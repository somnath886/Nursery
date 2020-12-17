from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Plant
from .serializers import SavePlantSerializer
from .helpers import jwtAuth

class AddPlant(APIView):
    
    def post(self, request):
        user = jwtAuth(request.headers)
        if user.is_nursery_user is False:
            return Response({"AuthorizationError": "Not Authorized"}, status=401)
        else:
            modifiedData = request.data
            modifiedData['Seller'] = user.id
            serializer = SavePlantSerializer(data=modifiedData)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)

class GetPlant(APIView):

    def get(self, request):
        allPlants = Plant.objects.all()
        list = []
        for plant in allPlants:    
            serializer = SavePlantSerializer(plant)
            list.append(serializer.data)
        return Response({"allPlants": list}, status=200)

    def get(self, request, name):
        findPlants = Plant.objects.filter(name=name)
        list = []
        for plant in findPlants:    
            serializer = SavePlantSerializer(plant)
            list.append(serializer.data)
        return Response({"plantsFound": list}, status=200)
