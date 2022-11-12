from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from car_exchange_app.models import *


class SubCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    sub_category = SubCategorySerializers(many=True)

    class Meta:
        model = Category
        fields = '__all__'


class AnswerSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Answer
        fields = '__all__'


class QuestionDetailSerializers(serializers.ModelSerializer):
    answers = AnswerSerializers(many=True)

    class Meta:
        model = Question
        fields = '__all__'


class QuestionCreateSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Question
        fields = '__all__'


class CarListSerializers(serializers.ModelSerializer):
    category = CategorySerializers(many=True)
    seller = serializers.HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Car
        fields = '__all__'


class CarDetailSerializers(serializers.ModelSerializer):
    """ Car detail """
    questions = QuestionDetailSerializers(many=True, read_only=True)
    category = CategorySerializers(many=True)
    seller = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = Car
        fields = '__all__'
