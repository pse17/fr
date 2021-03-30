from rest_framework import serializers


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ['title', 'begin', 'end', 'description']


class QuestionSerializer(serializers.ModelSerializer):
    poll = PollSerializer()

    class Meta:
        model = Question
        fields = ['title', 'option', 'poll']


class AnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = Answer
        fields = ['user', 'answer', 'question']
