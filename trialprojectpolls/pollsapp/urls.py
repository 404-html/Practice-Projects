from django.urls import path
from . import views

app_name = 'pollsapp'
#This is the list of urls for the PollsApp
urlpatterns = [
	#for the main page Ex. /polls/
	path('', views.IndexView.as_view(), name='index'),
	# Ex. /polls/1/
	path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
	# Ex. /polls/1/results/
	path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
	# Ex. /polls/1/vote/
	path('<int:question_id>/vote/', views.vote, name='vote'),

	]
