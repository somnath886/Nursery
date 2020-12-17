from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .helpers import jwtAuth
from .models import User, Plant, Order
from .serializers import SaveOrderSerializer, ViewOrderSerializer

class OrderPlant(APIView):
    
    def post(self, request):
        user = jwtAuth(request.headers)
        if user.is_normal_user is False:
            return Response({"authorizationError": "Not Authorized"}, status=401)
        else:
            seller = User.objects.get(id=request.data['sellerId'])
            plant = Plant.objects.get(name=request.data['orderedItem'])
            modifiedData = request.data
            modifiedData['orderedItem'] = plant.id
            modifiedData['sellerId'] = seller.id
            modifiedData['buyer'] = user.username
            print(modifiedData)
            serializer = SaveOrderSerializer(data=modifiedData)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)

class ViewOrders(APIView):

    def get(self, request):
        user = jwtAuth(request.headers)
        if user.is_nursery_user == False:
            return Response({"authorizationError": "Not Authorized"}, status=401)
        else:
            orders = Order.objects.filter(sellerId=user.id)
            list = []
            responseData = {'buyer': '', 'item': ''}
            for order in orders:
                responseData['buyer'] = order.buyer
                plant = Plant.objects.get(id=order.orderedItem.id)
                responseData['item'] = plant.name
                serializer = ViewOrderSerializer(responseData)
                list.append(serializer.data)
            return Response({"Orders": list}, status=201)