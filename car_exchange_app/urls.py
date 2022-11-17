from django.urls import path, include
from rest_framework import routers

from . import views

# router = routers.SimpleRouter()
# router.register(r'car', views.CarViewSet)

urlpatterns = [
    path('cars/', views.CarListCreateView.as_view(), name='cars'),
    path('cars/<int:pk>/', views.CarUpdateDestroyView.as_view()),
    path('question/', views.QuestionCreateView.as_view()),
    path('answer/', views.AnswerCreateView.as_view()),
    path('message/', views.MessageListView.as_view()),
    path('message/<int:pk>/', views.MessageDetailView.as_view()),
    path('wishlist/', views.WishListUpdateDetailView.as_view()),
    path('wish/<int:pk>/', views.WishCreateDelete.as_view()),
]