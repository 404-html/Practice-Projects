from django.shortcuts import render
from django.http import HttpResponse

def index(request): #This is the home page of the Website
	return HttpResponse("<h1>Hello World. You are at the polls index.</h1>")
