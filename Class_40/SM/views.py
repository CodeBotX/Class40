from django.shortcuts import render
from .models import *
# from rest_framework import viewsets
# from .models import DailySchedule
from .forms import *
from django.contrib import messages
from django.db import IntegrityError

def school_view(request):
    return render(request, 'school.html')

# Thêm môn học
def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thêm môn học thành công!')
    else:
        form = SubjectForm()

    return render(request, 'add_subjects.html', {'add_subjectForm': form})
# Thêm lớp học
def add_and_set_classroom(request):
    if request.method == 'POST':
        form_addClassroom = ClassroomForm(request.POST)
        form_setSubject = ClassoomSubjectForm(request.POST)
        if form_addClassroom.is_valid():
            action = request.POST.get('action')
            if action == 'addclassroom':
                form_addClassroom.save()
                messages.success(request, 'Thêm lớp học thành công!')
        elif form_setSubject.is_valid():
            action = request.POST.get('action')
            if action == 'setsubject':
                form_setSubject.save()
                messages.success(request,'Thành Công')
    else:
        form_addClassroom = ClassroomForm()
        form_setSubject = ClassoomSubjectForm()
    return render(request, 'add_classrooms.html', {'add_classroomForm': form_addClassroom, 'set_subjects':form_setSubject})

# Cài đặt tiết học ( giờ )
def add_lesson_time(request):
    if request.method == 'POST':
        form = LessonTimeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thêm thời gian học thành công!')
    else:
        form = LessonTimeForm()
    return render(request, 'time_table.html', {'add_lesson_timeForm': form})

# Thêm học sinh
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thêm học sinh thành công!')
    else:
        form = StudentForm()

    return render(request, 'add_students.html', {'add_studentForm': form})



# Thêm thời khóa biểu
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