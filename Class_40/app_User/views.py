from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from .forms import *

# Create your views here.

# User = get_user_model()
def teacher_register(request):
  form = SignUpForm()
  template = loader.get_template('signup.html')
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('home/')
  context = {
    'signupForm': form
  }
  return HttpResponse(template.render(context,request))

def teacher_login_home(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/success/')  # Thay đổi thành URL của trang thành công
    else:
        form = LoginForm()
    return render(request, 'login.html', {'loginForm': form})