from django.urls import path

from quizapp.accounts.views import RegisterApiView, CustomTokenObtainPairView, LogoutApiView, DeleteUserApiView, \
    UserListView, PasswordChangeView

app_name = 'accounts'

urlpatterns = (
    path('register/', RegisterApiView.as_view(), name='api register user'),
    path('login/', CustomTokenObtainPairView.as_view(), name='api login user'),
    path('logout/', LogoutApiView.as_view(), name='api logout user'),
    path('delete/', DeleteUserApiView.as_view(), name='api delete user'),
    path('change-password/', PasswordChangeView.as_view(), name='api change password'),
    path('list-users/', UserListView.as_view(), name='api list users'),

)
