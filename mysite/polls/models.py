import datetime

from django.db import models
from django.utils import timezone

class Subject(models.Model):
    Name = models.CharField(max_length=20)

    def __str__(self):
        return self.Name
    
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    dificulty = models.CharField(max_length=15)
    SubjectID = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    IsRight = models.BooleanField()
    QuestionID = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

class Users(models.Model):
    FIO = models.CharField(max_length=100)

    def __str__(self):
        return self.FIO

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Results(models.Model):
    UsersID = models.ForeignKey(Users, on_delete=models.CASCADE)
    QuestionID = models.ForeignKey(Question, on_delete=models.CASCADE)
    Rating =models.FloatField(verbose_name="Оценка")
   
    def __str__(self):
        return self.Resultes

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'

# Create your models here.