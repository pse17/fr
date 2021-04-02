from rest_framework import serializers


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['title', 'option']


class QuestionByPollsSeriazizer(serializers.ModelSerializer):
    poll = PollSerializer()

    class Meta:
        model = Question
        fields = ['poll']
        read_only_fields = ['title', 'option']


class AnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = Answer
        fields = ['user', 'answer', 'question']
