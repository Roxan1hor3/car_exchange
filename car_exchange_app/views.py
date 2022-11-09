from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Car, Question
from .permissions import IsOwnerOrReadOnly
from .serializers import QuestionListSerializers, CarDetailSerializers, CarListSerializers


class CarListCreateView(ListCreateAPIView):
    serializer_class = CarListSerializers

    def get_queryset(self):
        return Car.objects.select_related('drivetrain', 'color', 'year', 'transmission', 'seller', 'renge_mileage',
                                          'mark', 'body_type').prefetch_related('questions__answers')


class CarUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializers
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Car.objects.filter(pk=self.kwargs['pk']).select_related('drivetrain', 'color', 'year', 'transmission',
                                                                       'seller', 'renge_mileage',
                                                                       'mark', 'body_type').prefetch_related(
            'questions').prefetch_related('questions__answers')


class QuestionListCreateView(ListCreateAPIView):
    serializer_class = QuestionListSerializers

    def get_queryset(self):
        return Question.objects.filter(user=self.request.user).prefetch_related('answers')
# class CarListView(APIView):
#     """ All cars """
#
#     @staticmethod
#     def get(request):
#         cars = Car.objects.all()
#         serializers = CarListSerializers(cars, many=True)
#         return Response(serializers.data)
#
#
# class CarDetailView(APIView):
#     """ All cars """
#
#     @staticmethod
#     def get(request, pk):
#         cars = get_object_or_404(Car, pk=pk)
#         serializers = CarDetailSerializers(cars)
#         return Response(serializers.data)
