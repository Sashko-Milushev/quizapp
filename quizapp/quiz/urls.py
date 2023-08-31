from django.urls import path

from quizapp.quiz.views import StartQuizSession, RankingListView

app_name = 'quiz'

urlpatterns = (
    path('start-quiz-session/', StartQuizSession.as_view(), name='api start quiz session'),
    path('ranking/', RankingListView.as_view(), name='api ranking list')
)