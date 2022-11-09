from rest_framework import serializers

from car_exchange_app.models import *


class AnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionDetailSerializers(serializers.ModelSerializer):
    answers = AnswerSerializers(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'


class QuestionListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class CarListSerializers(serializers.ModelSerializer):
    body_type = serializers.SlugRelatedField(slug_field='title', queryset=BodyType.objects.all())
    mark = serializers.SlugRelatedField(slug_field='title', queryset=Mark.objects.all())
    renge_mileage = serializers.PrimaryKeyRelatedField(queryset=Mileage.objects.all())
    seller = serializers.HiddenField(default=serializers.CurrentUserDefault())
    transmission = serializers.SlugRelatedField(slug_field='title', queryset=Transmission.objects.all())
    year = serializers.PrimaryKeyRelatedField(queryset=Year.objects.all())
    color = serializers.SlugRelatedField(slug_field='title', queryset=Color.objects.all())
    drivetrain = serializers.SlugRelatedField(slug_field='title', queryset=Drivetrain.objects.all())
    questions = QuestionDetailSerializers(many=True, read_only=True)

    class Meta:
        model = Car
        fields = '__all__'

class CarDetailSerializers(serializers.ModelSerializer):
    """ Car detail """
    body_type = serializers.SlugRelatedField(slug_field='title', queryset=BodyType.objects.all())
    mark = serializers.SlugRelatedField(slug_field='title', queryset=Mark.objects.all())
    renge_mileage = serializers.PrimaryKeyRelatedField(queryset=Mileage.objects.all())
    seller = serializers.HiddenField(default=serializers.CurrentUserDefault())
    transmission = serializers.SlugRelatedField(slug_field='title', queryset=Transmission.objects.all())
    year = serializers.PrimaryKeyRelatedField(queryset=Year.objects.all())
    color = serializers.SlugRelatedField(slug_field='title', queryset=Color.objects.all())
    drivetrain = serializers.SlugRelatedField(slug_field='title', queryset=Drivetrain.objects.all())
    questions = QuestionDetailSerializers(many=True, read_only=True)

    class Meta:
        model = Car
        fields = '__all__'