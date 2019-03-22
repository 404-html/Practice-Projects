# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from appTwo.models import User
from appTwo.forms import myform

def index(request):
    return render(request, 'index.html')

def table(request):
    users = User.objects.all()
    dict = {'insert': users}
    return render(request, 'appTwo/table.html', context=dict)

def form(request):
    form = myform

    if request.method == 'POST':
        form = myform(request.POST)

        if form.is_valid():
            print(form.cleaned_data['first_name'])
            user = User.objects.get_or_create(first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], email=form.cleaned_data['email'])

    return render(request, 'appTwo/form.html', {'form':form})
