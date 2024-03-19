


# 
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from .forms import *
from CM.models import Student

# 
def teacher_register(request):
  form = SignUpForm()
  template = loader.get_template('signup.html')
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('Home_Login')
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
                return HttpResponseRedirect('home/')  # Thay đổi thành URL của trang thành công
    else:
        form = LoginForm()
    return render(request, 'login.html', {'loginForm': form})
  
def student_lookup_form(request):
    if request.method == 'POST':
        form = StudentLookupForm(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data['student_id']
            return redirect('LookUP', student=student_id)
    else:
        form = StudentLookupForm()
    return render(request, 'login.html', {'lookupForm': form})