from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizCategoryViewSet, QuizViewSet, QuestionViewSet, QuizAttemptViewSet, RatingViewSet, UserProgressViewSet, QuizTakingView

router = DefaultRouter()
router.register('quiz-categories', QuizCategoryViewSet)
router.register('quizzes', QuizViewSet)
router.register('questions', QuestionViewSet)
router.register('quiz-attempts', QuizAttemptViewSet)
router.register('ratings', RatingViewSet)
router.register('user-progress', UserProgressViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('quiz-taking/', QuizTakingView.as_view(), name='quiz-taking'),
]
