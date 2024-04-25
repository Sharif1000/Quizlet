from rest_framework import viewsets
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Quiz, QuizCategory, Question, QuizAttempt, Rating, UserProgress
from .serializers import QuizSerializer, QuizCategorySerializer, QuestionSerializer, QuizAttemptSerializer, RatingSerializer, UserProgressSerializer
from rest_framework.pagination import PageNumberPagination
from django.core.mail import send_mail


class QuizCategoryViewSet(viewsets.ModelViewSet):
    queryset = QuizCategory.objects.all()
    serializer_class = QuizCategorySerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuestionPagination(PageNumberPagination):
    page_size = 1
    
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    pagination_class = QuestionPagination
    
    
class QuizAttemptViewSet(viewsets.ModelViewSet):
    queryset = QuizAttempt.objects.all()
    serializer_class = QuizAttemptSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class UserProgressViewSet(viewsets.ModelViewSet):
    queryset = UserProgress.objects.all()
    serializer_class = UserProgressSerializer

class QuizTakingView(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def get_object(self):
        return self.queryset.first()
    
    def post(self, request, *args, **kwargs):
        quiz = self.get_object()
        user = request.user
        
        quiz_attempt = QuizAttempt.objects.create(
            user=user,
            quiz=quiz,
            score=0
        )
        
        selected_choices = request.data.get('selected_choices', {})
        total_score = 0
        total_questions = quiz.question_set.count()
        for question in quiz.question_set.all():
            correct_choice = question.correct_ans
            user_choice = selected_choices.get(str(question.id))
            if user_choice == correct_choice:
                total_score += 1
            
        quiz_attempt.score = total_score
        quiz_attempt.save()

        send_mail(
            'Quiz Completion',
            f'You have completed the quiz "{quiz.title}". Your score is {total_score}',
            'sharif.dupharmacy1@gmail.com',
            [user.email],
            fail_silently=False,
        )

        return Response({'message': 'Quiz completed successfully', 'score': total_score}, status=status.HTTP_200_OK)
