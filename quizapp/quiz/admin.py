from django.contrib import admin

from quizapp.quiz.models import QuizCategory


@admin.register(QuizCategory)
class QuizCategoryAdmin(admin.ModelAdmin):
    pass
