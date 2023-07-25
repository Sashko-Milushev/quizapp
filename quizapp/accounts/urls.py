from django.urls import path

from quizapp.accounts.views import RegisterApiView, CustomTokenObtainPairView, LogoutApiView

app_name = 'accounts'

urlpatterns = (
    path('register/', RegisterApiView.as_view(), name='api register user'),
    path('login/', CustomTokenObtainPairView.as_view(), name='api login user'),
    path('logout/', LogoutApiView.as_view(), name='api logout user'),

)
