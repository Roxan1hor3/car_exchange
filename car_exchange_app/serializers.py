from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from car_exchange_app.models import *
from car_exchange_app.services.services import add_tag_to_text_question, message_create


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
        fields = ('id', 'updated_at', 'text_question', 'user', 'car', 'question', 'parent', 'created_at', 'updated_at')

    def create(self, validated_data):
        answer = add_tag_to_text_question(validated_data)
        message_create(validated_data)
        return answer


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
        fields = '__all__'#['created_at', 'phone', 'other_photo', 'description_accidents']


class CarDetailSerializers(serializers.ModelSerializer):
    """ Car detail """
    questions = QuestionDetailSerializers(many=True, read_only=True)
    category = CategorySerializers(many=True)
    seller = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Car
        fields = '__all__'


class MessageListSerializers(serializers.ModelSerializer):
    car = serializers.SlugRelatedField('name', read_only=True)

    class Meta:
        model = Message
        fields = ('updated_at', 'text_message', 'car', 'question', 'answer')


class MessageDetailSerializers(serializers.ModelSerializer):
    car = CarDetailSerializers()
    ping = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ('updated_at', 'text_message', 'car', 'question', 'answer', 'ping')

    def get_ping(self, obj):
        if obj.answer:
            return AnswerSerializers(obj.answer).data
        else:
            return AnswerSerializers(obj.question).data


class WishSerializers(serializers.ModelSerializer):
    car = serializers.SlugRelatedField(slug_field='name', queryset=Car.objects.all())

    class Meta:
        model = Wish
        fields = '__all__'
