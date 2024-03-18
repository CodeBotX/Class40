from django.shortcuts import render,redirect
from django.template import loader
from .forms import *
from .models import *
from django.shortcuts import get_object_or_404, render
from SM.models import Classroom as SM_Classroom
from SM.models import LessonTime 
from SM.models import DailySchedule
from SM.models import ScheduleEntry
from SM.models import Subject
from django.utils import timezone
from datetime import datetime
from django.contrib.auth import get_user_model
from django.contrib import messages

day_names = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ Nhật"]


# Create your views here.

def home(request):
    # Giáo viên chọn Lớp học
    template = loader.get_template('home.html')
    if request.method == 'GET':
        classroom = request.GET.get('classroom')
        if classroom:
            return redirect('classroom', classroom=classroom)
    classrooms = SM_Classroom.objects.all()
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
    classroom = get_object_or_404(SM_Classroom, name=classroom) # đưa vào add lesson
    seats = classroom.seats.all().order_by('row', 'column') # đưa vào add lesson
    period = get_period() # tiết test
    now_subject = get_subject(classroom=classroom, period= period) 
    now = timezone.now().time()
    day_number = datetime.now().weekday()
    day_name = day_names[day_number]
    User = get_user_model()
    teacher = teacher = request.user
    if request.method == 'POST':
        form_addlesson = LessonForm(request.POST, teacher=teacher)
        if form_addlesson.is_valid():
            lesson = form_addlesson.save(commit=False)
            lesson.classroom = classroom
            lesson.subject = now_subject
            lesson.save()
            messages.success(request, 'Thành công!')
    else:
        form_addlesson = LessonForm(teacher=teacher)
    context = {
        'rows': range(1, 6),
        'columns': range(1, 9),
        'classroom': classroom,
        'seats':seats,
        'now_subject':now_subject.name,
        'period':period,
        'now':now,
        'day_of_week':day_name,
        'form_addlesson': form_addlesson
    }
    return render(request, 'classroom.html', context)

def get_period():

    now = timezone.now().time()  # Lấy chỉ thời gian, không lấy ngày
    # Truy vấn database để tìm tiết học mà thời gian hiện tại nằm giữa thời gian bắt đầu và kết thúc
    lesson = LessonTime.objects.filter(start_time__lte=now, end_time__gte=now).first()
    if lesson:
        # Nếu tìm thấy tiết học, trả về thông tin tiết học
        return f"{lesson.period}"
    else:
        # Nếu không tìm thấy tiết học nào, có nghĩa là hiện tại không phải thời gian học
        return "Hiện tại không phải thời gian học."
    

# Trả về môn học đang học
def get_subject(classroom, period):
    classroom = get_object_or_404(SM_Classroom, name=classroom)
    day_number = datetime.now().weekday()
    # Tìm DailySchedule tương ứng với classroom và ngày hiện tại
    daily_schedule = DailySchedule.objects.filter(classroom=classroom, day_of_week=day_number).first()
    if not daily_schedule:
        return False
    else:
        schedule_entry = ScheduleEntry.objects.filter(daily_schedule=daily_schedule, period__period=period).first()
        if not schedule_entry:
            return False
    return schedule_entry.subject
        
