from django.contrib import admin
from django.urls import path,include
from voting import views
from .views import logout_user
urlpatterns = [
  path('', views.index, name='index'),
  path('voting.html', views.voting, name='voting'),
  path('index.html', views.index, name='index'),
  path('contact.html', views.contact, name='contact'),
  path('login.html', views.login_user, name='login_user'),
  path('signup.html', views.signup, name='signup'),
  path('logout', views.logout_user, name='logout'),
  path('send_vote<str:candidatename>', views.send_vote, name='send_vote'),
  path('result.html', views.result, name='result'),
]