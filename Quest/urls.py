from django.contrib import admin
from django.urls import path, include
from Quest.views import *


app_name = 'Quest'
urlpatterns = [
    path('quest/create/', QuestCreateView.as_view()),
    path('all/', QuestListView.as_view()),
    path('quest/detail/<int:pk>/', QuestDetailView.as_view()),
]