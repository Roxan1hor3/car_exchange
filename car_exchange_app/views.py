from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from .models import Car
from .permissions import IsOwnerOrReadOnly
from .serializers import CarDetailSerializers, CarListSerializers, QuestionCreateSerializers, AnswerSerializers


class CarListCreateView(ListCreateAPIView):
    serializer_class = CarListSerializers

    def get_queryset(self):
        return Car.objects.select_related('seller').prefetch_related('questions__answers', 'category__sub_category')


class CarUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializers
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Car.objects.filter(pk=self.kwargs['pk']).prefetch_related('questions__answers', 'category')


class QuestionCreateView(CreateAPIView):
    serializer_class = QuestionCreateSerializers


class AnswerCreateView(CreateAPIView):
    serializer_class = AnswerSerializers

