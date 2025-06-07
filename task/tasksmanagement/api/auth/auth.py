from rest_framework.generics import CreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import AllowAny

class UserCreateView(CreateAPIView):
    """
    API View to create a new user
    """
    permission_classes = [AllowAny]


    def post(self, request: Request, *args, **kwargs) -> Response:
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'message': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        hashed_password = make_password(password)

        _ , created = User.objects.get_or_create(username=username, password=hashed_password)

        if created:
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)




