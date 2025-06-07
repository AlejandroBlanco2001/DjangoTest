from django.urls import path
from .auth import UserCreateView
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('/register', UserCreateView.as_view(), name='user-create'),
    path('/login', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]