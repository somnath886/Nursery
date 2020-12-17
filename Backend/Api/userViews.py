from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from django.http import JsonResponse
import hashlib
import jwt

from .models import User
from .serializers import SaveUserSerializer
from .helpers import verifyNurseryLogin, verifyNormalLogin, jwtAuth

class RegisterNurseryUser(APIView):

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        username = body['username']
        getUser = User.objects.filter(username=username)
        if len(getUser) == 0:
            modifiedData = request.data
            hashed_password = modifiedData['password']
            result = hashlib.sha256(hashed_password.encode())
            modifiedData['password'] = result.hexdigest()
            modifiedData['is_nursery_user'] = True
            serializer = SaveUserSerializer(data=modifiedData)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
        else:
            return Response({"error": "user already exists"})

class RegisterNormalUser(APIView):

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        username = body['username']
        getUser = User.objects.filter(username=username)
        if len(getUser) == 0:
            modifiedData = request.data
            hashed_password = modifiedData['password']
            result = hashlib.sha256(hashed_password.encode())
            modifiedData['password'] = result.hexdigest()
            modifiedData['is_normal_user'] = True
            serializer = SaveUserSerializer(data=modifiedData)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
        else:
            return Response({"error": "user already exists"})

class LoginNurseryUser(APIView):

    def post(self, request):
        error = verifyNurseryLogin(request.data)
        if len(error.keys()) == 0:
            encoded_jwt = jwt.encode({'username': request.data['username']}, 'secret', algorithm='HS256')
            return Response({"Token": encoded_jwt}, status=201)

        else:
            return Response(error, status=401)

class LoginNormalUser(APIView):

    def post(self, request):
        error = verifyNormalLogin(request.data)
        if len(error.keys()) == 0:
            encoded_jwt = jwt.encode({'username': request.data['username']}, 'secret', algorithm='HS256')
            return Response({"Token": encoded_jwt}, status=201)

        else:
            return Response(error, status=401)

class HelloWorldNursery(APIView):

    def get(self, request):
        user = jwtAuth(request.headers)
        if user.is_nursery_user == False:
            return Response({"AuthorizationError": "Not Authorized"}, status=401)
        else:
            return Response({"Hello": "World"}, status=201)

class HelloWorldNormal(APIView):

    def get(self, request):
        user = jwtAuth(request.headers)
        if user.is_normal_user == False:
            return Response({"AuthorizationError": "Not Authorized"}, status=401)
        else:
            return Response({"Hello": "World"}, status=201)
