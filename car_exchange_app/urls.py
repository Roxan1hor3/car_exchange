from django.urls import path, include
from rest_framework import routers

from . import views

# router = routers.SimpleRouter()
# router.register(r'car', views.CarViewSet)

urlpatterns = [
    path('cars/', views.CarListCreateView.as_view()),
    path('cars/<int:pk>/', views.CarUpdateDestroyView.as_view()),
    path('question/', views.QuestionCreateView.as_view()),
    path('answer/', views.AnswerCreateView.as_view()),
]