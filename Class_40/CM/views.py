from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .forms import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404, render


# Create your views here.

def home_view(request):
    # Giáo viên chọn Lớp học
    template = loader.get_template('home.html')
    if request.method == 'GET':
        classroom = request.GET.get('classroom')
        if classroom:
            return redirect('classroom', classroom=classroom)
    classrooms = Classroom.objects.all()
    return render(request, 'home.html', {'classrooms': classrooms})



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

def classroom(request, classroom):
    # Hiển thị học sinh trong lớp
    classroom = get_object_or_404(Classroom, name=classroom)
    students = classroom.student.all()
    return render(request, 'classroom.html', {'classroom': classroom, 'student': students})
