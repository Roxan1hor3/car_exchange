from rest_framework import mixins
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView, \
    GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import BrowsableAPIRenderer

from .models import Car, Message, Wish
from .permissions import IsOwnerOrReadOnly
from .serializers import CarDetailSerializers, CarListSerializers, QuestionCreateSerializers, \
    AnswerSerializers, MessageListSerializers, MessageDetailSerializers, WishSerializers
from .services.castome_responce import CarRenderer, MessageRenderer
from .services.objects_services import all_objects, filter_objects


class CarListCreateView(ListCreateAPIView):
    serializer_class = CarListSerializers
    renderer_classes = [CarRenderer, BrowsableAPIRenderer]

    def get_queryset(self):
        return all_objects(
            objects=Car.objects,
            select_related=('seller',),
            prefetch_related=('questions__answers__user', 'category__sub_category'),
        )


class CarUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializers
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return filter_objects(
            objects=Car.objects,
            pk=self.kwargs['pk'],
            prefetch_related=('questions__answers__user', 'category__sub_category')
        )


class QuestionCreateView(CreateAPIView):
    serializer_class = QuestionCreateSerializers


class AnswerCreateView(CreateAPIView):
    serializer_class = AnswerSerializers


class MessageListView(ListAPIView):
    serializer_class = MessageListSerializers
    permission_classes = [IsAuthenticated]
    renderer_classes = [MessageRenderer, BrowsableAPIRenderer]

    def get_queryset(self):
        return filter_objects(
            objects=Car.objects,
            user=self.request.user,
            select_related=('car',)
        )


class MessageDetailView(ListAPIView):
    serializer_class = MessageDetailSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return filter_objects(
            objects=Message.objects,
            pk=self.kwargs['pk'],
        )


class WishListUpdateDetailView(ListAPIView):
    serializer_class = WishSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return filter_objects(
            objects=Wish.objects,
            user=self.request.user,
            prefetch_related=('car__category__sub_category',)
        )


class WishCreateDelete(mixins.DestroyModelMixin,
                       mixins.CreateModelMixin,
                       GenericAPIView):
    serializer_class = WishSerializers
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
