from car_exchange_app.models import Answer, Message


def add_tag_to_text_question(validated_data):
    if validated_data['parent']:
        parent = validated_data['parent']
        text_question = validated_data['text_question']
        text_question = f'@{parent.user.username} ' + text_question
        validated_data['text_question'] = text_question
    return Answer.objects.create(**validated_data)


def message_creata(validated_data):
    data = {}
    print(validated_data)
    text_message = """Someone answered you"""
    data['text_message'] = text_message
    data['car'] = validated_data['car']
    if validated_data['parent']:
        data['answer'] = validated_data['parent']
    data['question'] = validated_data['question']
    print(data)
    message = Message.objects.create(**data)
    message.user.add(validated_data['parent'].user, validated_data['question'].user)
