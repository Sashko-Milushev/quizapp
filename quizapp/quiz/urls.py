from django.urls import path

from quizapp.quiz.views import StartQuizSession

app_name = 'quiz'

urlpatterns = (
    path('start-quiz-session/', StartQuizSession.as_view(), name='api start quiz session'),
)