from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from quizapp.quiz.models import QuizCategory, QuizSession, Rank
from quizapp.quiz.opentdb_api_service import get_random_questions, get_questions_for_category
from quizapp.quiz.serializers import RankSerializer


class StartQuizSession(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        category_id = request.query_params.get('category_id')  # Get the category ID from query parameters

        # Get the category instance or return a 404 response if not found
        category = get_object_or_404(QuizCategory, id=category_id)

        # Fetch questions based on the user's choice
        if category.name == 'Random':
            quiz_questions = get_random_questions()
        else:
            quiz_questions = get_questions_for_category(category)

        return Response({'questions': quiz_questions}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user = request.user
        category_id = request.data.get('category_id')
        number_of_correct_answers = request.data.get('number_of_correct_answers')

        # Get the category instance or return a 404 response if not found
        category = get_object_or_404(QuizCategory, id=category_id)

        # Create a new QuizSession instance
        session = QuizSession.objects.create(
            user=user,
            category=category,
            correct_answers=number_of_correct_answers,
        )

        # Calculate and update points for the session
        session.calculate_points()

        # Update the user's rank after calculating and saving points
        Rank.update_rank(user=user)

        return Response({'points': session.points}, status=status.HTTP_201_CREATED)


class RankingListView(APIView):
    def get(self, request, *args, **kwargs):
        ranks = Rank.objects.all()
        serializer = RankSerializer(ranks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
