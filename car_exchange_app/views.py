from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from .models import Car
from .permissions import IsOwnerOrReadOnly
from .serializers import CarDetailSerializers, CarListSerializers, QuestionCreateSerializers, AnswerSerializers


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
                                                                       'seller', 'renge_mileage', 'mark',
                                                                       'body_type').prefetch_related(
            'questions__answers')


class QuestionCreateView(CreateAPIView):
    serializer_class = QuestionCreateSerializers


class AnswerCreateView(CreateAPIView):
    serializer_class = AnswerSerializers

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
