from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class QuizCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class QuizSession(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    correct_answers = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Session for {self.user.username} - Category: {self.category.name}"

    def calculate_points(self):
        self.points = self.correct_answers
        if self.correct_answers == 10:
            self.points += 5
        if self.category.name == 'RANDOM':
            self.points *= 2
        self.save()


class Rank(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, primary_key=True)
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Rank for {self.user.username}"

    @classmethod
    def update_rank(cls, user):
        user_sessions = QuizSession.objects.filter(user=user)
        total_points = user_sessions.aggregate(total_points=models.Sum('points'))['total_points']
        rank, created = cls.objects.get_or_create(user=user)
        rank.points = total_points if total_points else 0
        rank.save()

    class Meta:
        ordering = ['-points']
