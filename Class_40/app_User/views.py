# 
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from .forms import *
from SM.models import Mark, Student


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

# CŨ
# def teacher_login_home(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return HttpResponseRedirect('home/')  # Thay đổi thành URL của trang thành công
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'loginForm': form})

# -------------------------------------------------------------------------------------------------------

def Look_up(request, student):
<<<<<<< HEAD
    # Lấy thông tin sinh viên dựa trên student_id
    student_obj = get_object_or_404(student, id=student)
    
    # Lấy tất cả điểm của sinh viên này
    marks = Mark.objects.filter(student=student_obj)
    
    # Truyền dữ liệu vào template
    return render(request, 'lookup.html', {'marks': marks, 'student': student_obj})
=======
  # Lấy thông tin sinh viên dựa trên student_id
  student_obj = get_object_or_404(Student, id=student)
  
  # Lấy tất cả điểm của sinh viên này
  marks = Mark.objects.filter(student=student_obj)
  subject_scores = {}
  for mark in marks:
    subject_name = mark.subject.name
    scores = mark.scores
    if subject_name not in subject_scores:
        subject_scores[subject_name] = []
    subject_scores[subject_name].extend(scores)
  
  # Truyền dữ liệu vào template
  return render(request, 'lookup.html', {'marks': subject_scores, 'student': student_obj})
>>>>>>> 6aea3faec628f613ca210f484b08913db4730ad9


def teacher_login_home(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        lookup_form = StudentLookupForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('home/')  # Thay đổi thành URL của trang thành công
        elif lookup_form.is_valid():
            action = request.POST.get('action')  # Lấy giá trị của action từ form
            if action == 'check':  # Đổi thành 'check'
                student_id = lookup_form.cleaned_data['student_id']
                return redirect('Lookup', student=student_id)
    else:
        login_form = LoginForm()
        lookup_form = StudentLookupForm()
    return render(request, 'login.html', {'loginForm': login_form, 'lookupForm': lookup_form})