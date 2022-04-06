from django.contrib import admin
from django.urls import path

from core.polls.views import GetQuestion, QuestionAnswer

urlpatterns = [
    path('', GetQuestion.as_view()),
    path('answer/', QuestionAnswer.as_view()),
]
