from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include([
        path('token/', TokenObtainPairView.as_view(), name='api token obtain pair'),
        path('token/refresh', TokenRefreshView.as_view(), name='api token refresh'),
        path('quiz/', include('quizapp.quiz.urls')),
        path('accounts/', include('quizapp.accounts.urls')),
    ]))

]
