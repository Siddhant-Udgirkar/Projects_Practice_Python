from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class LoginView(APIView):
    def post(self, request):
        username= request.data.get("username")
        password= request.data.get("password")

        user= authenticate(username=username, password=password)

        if user is not None:
            token, created= Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request):
        username= request.data.get("username")
        password= request.data.get("password")

        user= authenticate(username=username, password=password)

        if user is not None:
            return Response(username, password, status=status.HTTP_200_OK)
