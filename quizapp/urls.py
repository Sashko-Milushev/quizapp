from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include([
        path('quiz/', include('quizapp.quiz.urls')),
        path('accounts/', include('quizapp.accounts.urls')),
    ]))

]
