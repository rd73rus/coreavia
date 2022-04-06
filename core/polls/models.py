from django.db import models
from django.conf import settings


class Question(models.Model):
    title = models.CharField(max_length=4096)
    visible = models.BooleanField(default=False)
    max_points = models.FloatField()

    class Meta:
        verbose_name_plural = 'Вопросы'
        verbose_name = 'Вопрос'

    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=4096)
    points = models.FloatField()
    lock_other = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Варианты'
        verbose_name = 'Вариант'

    def __str__(self):
        return self.title


class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choice = models.ForeignKey(Choice, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Ответы'
        verbose_name = 'Ответ'

    def __str__(self):
        return self.choice.title
