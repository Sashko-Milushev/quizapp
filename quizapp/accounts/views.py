from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import RevokedToken
from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserRegistrationSerializer

UserModel = get_user_model()


class RegisterApiView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class LogoutApiView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # Get the refresh token from the request data
            refresh_token = request.data['refresh_token']
            # Create a RefreshToken object from the provided token
            token = RefreshToken(refresh_token)
            # Blacklist the refresh token to effectively invalidate it
            # Check if the token is in the RevokedToken list
            if RevokedToken.objects.filter(token=refresh_token).exists():
                return Response({"detail": "Token has already been revoked."},
                                status=status.HTTP_400_BAD_REQUEST)

            # Add the token to the revoked tokens list
            RevokedToken.objects.create(token=refresh_token)
            return Response({"detail": "Logout successful."}, status=status.HTTP_200_OK)
        except KeyError:
            return Response({"detail": "Refresh token not provided."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"detail": "Invalid refresh token."}, status=status.HTTP_400_BAD_REQUEST)
