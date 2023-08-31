from django.contrib.auth.hashers import check_password
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import RevokedToken
from .serializers import CustomTokenObtainPairSerializer, PasswordChangeSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserRegistrationSerializer
from .utils import send_registration_email

UserModel = get_user_model()


# View for user registration
class RegisterApiView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        # Send welcome email to the user
        send_registration_email(user_email=user.email, user=user)


# View for user login with additional checks
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except AuthenticationFailed as e:
            # Check if user has deleted account
            if UserModel.objects.filter(email=request.data.get("email"), is_deleted=True).exists():
                raise AuthenticationFailed("Your account has been deleted.")
            raise e
        # Successful login with tokens in the response
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


# View for user loging out
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


# View for soft deleting user account
class DeleteUserApiView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = request.user
        # Change default value to preform the soft deletion
        user.is_deleted = True
        user.save()

        return Response({
            "detail": "User account has been marked as deleted."
        }, status=status.HTTP_204_NO_CONTENT)


# View for listing all active users
class UserListView(generics.ListAPIView):
    serializer_class = UserRegistrationSerializer

    # Filter only the active users
    def get_queryset(self):
        active_users = UserModel.objects.filter(is_deleted=False)
        return active_users


# View for password change
class PasswordChangeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = PasswordChangeSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']

            if not check_password(old_password, user.password):
                return Response({"detail": "Incorrect old password."},
                                status=status.HTTP_400_BAD_REQUEST)

            user.set_password(new_password)
            user.save()
            return Response({"detail": "Password changed successfully."},
                            status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
