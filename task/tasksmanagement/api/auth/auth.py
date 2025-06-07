from rest_framework.generics import CreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import AllowAny
from logging import getLogger
from django.db import IntegrityError

logger = getLogger(__name__)

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

        try:
            _ , created = User.objects.get_or_create(username=username, password=hashed_password)
        except IntegrityError as e:
            logger.error(f'Error creating user: {e}')
            return Response({'message': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)





