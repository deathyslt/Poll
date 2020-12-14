from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title} - {self.id}'


class Choice(models.Model):
    title = models.CharField(max_length=200)
    number = models.IntegerField()
    number_of_vote = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return f'{self.question.id} - {self.title}'


class Account(models.Model):
    account = models.OneToOneField(User, on_delete=models.RESTRICT)
    question = models.ManyToManyField(Question, through='Result')

    def __str__(self):
        return self.account.username


class Result(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, unique=True)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, unique=True)


def __str__(self):
    return f'{self.question.id} - {self.choice.number}'
