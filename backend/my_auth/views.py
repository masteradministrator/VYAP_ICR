from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate
from django.http import HttpResponse
from rest_framework import viewsets, permissions, status, generics, views
from rest_framework.authtoken.models import Token
from django.contrib.auth.tokens import default_token_generator
from rest_framework.response import Response
from my_auth.serializers import UserSerializer, LoginSerializer, TokenSerializer

User = get_user_model()

#class LoginView(viewsets.ModelViewSet, generics.UpdateAPIView):
 #   queryset = InwardCourierRegistry.objects.all()
 #   serializer_class = InwardCourierRegistrySerializer
class LoginView(views.APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.validate(request.data)
        user = serializer.user
        token, _ = Token.objects.get_or_create(user=user)
        data = TokenSerializer(token).data
        return Response(
            data=data,
            status=status.HTTP_200_OK,
        )

class RegisterViewSet(viewsets.ModelViewSet, generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
 
    def perform_create(self, serializer):
        serializer = UserSerializer(data=serializer.data)
        print(serializer.is_valid())
        print(serializer.errors)
        if serializer.is_valid():
            print(serializer.data.get('email'))
            instance = serializer.save()
