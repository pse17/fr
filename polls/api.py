import datetime
from rest_framework import generics
from rest_framework import viewsets
from polls import models, serializers


class PollView(viewsets.ModelViewSet):
    '''
    CRUD для опросов
    '''
    queryset = models.Poll.objects.all()
    serializer_class = serializers.PollSerializer
    permission_classes = []

class QuestionView(viewsets.ModelViewSet):
    '''
    CRUD для вопросов
    '''
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = []


class AddQuestionToPoll(viewsets.ModelViewSet):
    '''
    Связываем вопрос с опросом. Связь Many to Many.
    '''
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionByPollsSeriazizer
    permission_classes = []


class GetActivePolls(generics.ListAPIView):
    '''
    Получаем активные опросы. Poll.begin < datetime.now()
    '''
    queryset = models.Poll.objects.filter(poll <= datetime.datetime.now()).all()
    serializer_class = serializers.PollSerializer


class GetQuestionsByPoll(generics.ListAPIView):
    '''
    Получаем все вопросы в опросе
    '''
    serializer_class  = serializers.QuestionSerializer

    def get_queryset(self):
        return models.Poll.objects.filter(poll__pk=self.kwargs['pk']).all()


class GetAnswer(generics.CreateAPIView):
    '''
    Сохраняем ответ. 
    '''
    serializer_class = serializers.AnswerSerializer

    def perform_create(self, serializer):
        poll = models.Poll.objects.get(self.request.data['poll'])
        question = models.Question.objects.get(self.request.data['question'])

        serializer.save(poll=poll, question=question)


class GetAnswersByUserID(generics.ListAPIView):
    '''
    Получаем детализацию ответов по опросу, по пользователю.
    '''
    serializer_class = serializers.AnswerSerializer

    def get_queryset(self):
        return models.Answer.objects
            .filter(user=self.request.data['user'])
            .filter(poll__pk=self.request.data['poll'])
            .all()
