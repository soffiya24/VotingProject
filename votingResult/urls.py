from django.contrib import admin
from django.urls import path,include
from votingResult import views
urlpatterns = [
  path('', views.votingResult, name='votingResult'),
]