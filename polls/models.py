from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=256)
    begin = models.DateField(editable=False)
    end = models.DateField()
    description = models.TextField()


class Question(models.Model):
    title = models.CharField(max_length=256)

    ONE = 'o'
    MANY = 'm'
    TEXT = 't'
    TYPE_OF_ANSWER = [
        (ONE,'Ответ с выбором одного варианта'),
        (MANY,'Oтвет с выбором нескольких вариантов'),
        (TEXT,'Oтвет текстом')
    ]
    option = models.CharField(max_length=1, choices=TYPE_OF_ANSWER)
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE)


class Answer(models.Model):
    user = models.IntegerField()
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    answer = models.TextField()