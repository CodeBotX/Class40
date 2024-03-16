from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .forms import *
from django.contrib.auth import get_user_model 

# Create your views here.

def classroom_view(request):
    template = loader.get_template('classroom.html')
    return HttpResponse(template.render())

def test_view(request):
    template = loader.get_template('testForm.html')
    # form = SignUpForm()
    context = {
        #'signupForm': form
    }
    return HttpResponse(template.render())

def add_mark(request):
    if request.method == 'POST':
        form = MarkAddForm(request.POST)
        if form.is_valid():
            mark = form.cleaned_data['mark']
            # Thực hiện logic để thêm điểm vào cơ sở dữ liệu ở đây
            # Đừng quên lấy thông tin về student và subject từ request
            return redirect('success_url')  # Redirect người dùng sau khi thành công
    else:
        form = MarkAddForm()

    return render(request, 'testForm.html', {'add_markForm': form})