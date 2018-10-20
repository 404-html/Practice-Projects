from django.urls import path
from . import views

#This is the list of urls for the PollsApp
urlpatterns = [
	path('', views.index, name='index'),
	]
