from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from rest_framework import viewsets
from .models import DailySchedule
from .serializers import DailyScheduleSerializer
from .forms import *
from django.contrib import messages
from django.db import IntegrityError

def school_view(request):
    return render(request, 'school.html')


def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thêm môn học thành công!')
    else:
        form = SubjectForm()

    return render(request, 'add_subjects.html', {'add_subjectForm': form})

def add_classroom(request):
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thêm lớp học thành công!')
    else:
        form = ClassroomForm()

    return render(request, 'add_classrooms.html', {'add_classroomForm': form})

def add_lesson_time(request):
    if request.method == 'POST':
        form = LessonTimeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thêm thời gian học thành công!')
    else:
        form = LessonTimeForm()
    return render(request, 'time_table.html', {'add_lesson_timeForm': form})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thêm học sinh thành công!')
    else:
        form = StudentForm()

    return render(request, 'add_students.html', {'add_studentForm': form})




class DailyScheduleViewSet(viewsets.ModelViewSet):
    queryset = DailySchedule.objects.all()
    serializer_class = DailyScheduleSerializer

# xử lý người dùng add thời Khóa biểu 
# def add_schedule(request):
#     if request.method == 'POST':
#         form = ScheduleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Thêm lịch học thành công!')
#     else:
#         form = ScheduleForm()

#     return render(request, 'time_table.html', {'form': form})

def add_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Thêm lịch học thành công!')
            except IntegrityError:
                messages.error(request, 'Lỗi: Tiết học này đã được thêm rồi.')
    else:
        form = ScheduleForm()

    return render(request, 'time_table.html', {'timetable_form': form})