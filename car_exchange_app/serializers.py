from rest_framework import serializers

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
    answers = AnswerSerializers(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'


class QuestionCreateSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Question
        fields = '__all__'


class CarListSerializers(serializers.ModelSerializer):
    questions = QuestionDetailSerializers(many=True, read_only=True)
    category = CategorySerializers(many=True)

    class Meta:
        model = Car
        fields = '__all__'


class CarDetailSerializers(serializers.ModelSerializer):
    """ Car detail """
    questions = QuestionDetailSerializers(many=True, read_only=True)
    category = CategorySerializers(many=True, read_only=True)

    class Meta:
        model = Car
        fields = '__all__'
