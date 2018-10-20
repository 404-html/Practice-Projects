from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Choice, Question
from django.urls import reverse
from django.views import generic

class IndexView(generic.ListView): #This is the home page of the Website
	template_name = 'pollsapp/index.html'
	context_object_name = 'latest_question_list'
	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
	model = Question
	template_name = 'pollsapp/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'pollsapp/results.html'

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		#Redisplay the question voting form.
		return render( request, 'pollsapp/detail.html'), {'question':question, 'error_message': "You did not select a choice"}
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('pollsapp:results', args=(question.id,)))

