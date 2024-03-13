from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .forms import *
from django.contrib.auth import get_user_model 

# Create your views here.

def classroom_view(request):
    template = loader.get_template('classroom.html')
    return HttpResponse(template.render())

