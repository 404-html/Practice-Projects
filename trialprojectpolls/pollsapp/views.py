from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Choice, Question
from django.urls import reverse

def index(request): #This is the home page of the Website
	latest_questions_list = Question.objects.order_by('-pub_date')[ :5]
	context = { 'latest_questions_list' : latest_questions_list	}
	return render(request, 'pollsapp/index.html', context)

def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render (request, 'pollsapp/detail.html', {'question': question})

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'pollsapp/results.html', {'question': question})

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

