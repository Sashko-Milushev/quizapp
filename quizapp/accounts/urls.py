from django.urls import path

from quizapp.accounts.views import RegisterApiView

app_name = 'accounts'

urlpatterns = (
    path('register/', RegisterApiView.as_view(), name='api register user'),


)
