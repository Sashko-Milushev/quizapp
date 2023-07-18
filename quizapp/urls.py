
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/', include('quizapp.quiz.urls')),
    path('auth/', include('quizapp.accounts.urls')),
]
