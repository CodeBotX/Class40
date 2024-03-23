from django.shortcuts import render,redirect
from django.template import loader
from .forms import *
from .models import *
from django.shortcuts import get_object_or_404, render
from SM.models import Classroom
from SM.models import LessonTime 
from SM.models import TableSchedule
from SM.models import Student
from SM.models import Mark
from SM.models import *
from datetime import datetime,timedelta
from django.contrib.auth import get_user_model
from django.contrib import messages

day_names = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ Nhật"]
day_namese = ["Monday", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Sunday"]


# home - chọn lớp học, dạy học or tổng kết
def home(request):
    # Giáo viên chọn Lớp học
    template = loader.get_template('home.html')
    if request.method == 'GET':
        classroom = request.GET.get('classroom')
        action = request.GET.get('action')
        if classroom:
            if action == 'Dạy Học':
                return redirect('classroom', classroom=classroom)
            elif action == 'Tổng Kết':
                return redirect('summary', classroom=classroom)
    classrooms = Classroom.objects.all()
    return render(request, 'home.html', {'classrooms': classrooms})


# Thêm Điểm
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

# classroom  - Hiển thị sơ đồ lớp, Môn Học, Tiết Học, Kì học
def classroom(request, classroom):
    # Hiển thị học sinh trong lớp
    classroom = get_object_or_404(Classroom, name=classroom) # đưa vào add lesson
    seats = classroom.seats.all().order_by('row', 'column') # đưa vào add lesson
    nowsubject = get_nowsubject(classroom=classroom)
    now = datetime.now()
    # Lấy thứ
    day_number = datetime.now().weekday()
    day_name = day_names[day_number]
    
    teacher = teacher = request.user
    
    period = LessonTime.objects.filter(start_time__lte=now, end_time__gte=now).first()

    # , dayofweek=day_number, period=period
    if request.method == 'POST':
        form_addlesson = LessonForm(request.POST, teacher=teacher)
        if form_addlesson.is_valid():
            lesson = form_addlesson.save(commit=False)
            lesson.classroom = classroom
            lesson.subject = nowsubject
            lesson.save()
            messages.success(request, 'Thành công!')
    else:
        form_addlesson = LessonForm(teacher=teacher)
    context = {
        'rows': range(1, 6),
        'columns': range(1, 9),
        'classroom': classroom,
        'seats':seats,
        'now':now,
        'subject':nowsubject,
        'day_of_week':day_name,
        'form_addlesson': form_addlesson,
        'period':period
    }
    return render(request, 'classroom.html', context)


# Trả về tiết học ở thời gian thực 
def get_nowsubject(classroom):
    dayofweek = datetime.now().weekday()
    now = datetime.now()
    # Truy vấn database để tìm tiết học mà thời gian hiện tại nằm giữa thời gian bắt đầu và kết thúc
    period = LessonTime.objects.filter(start_time__lte=now, end_time__gte=now).first()
    schedule = TableSchedule.objects.filter(classroom=classroom,dayofweek=dayofweek, period=period).first()
    if schedule:
        return schedule.subject
    else:
        return None


# Giáo viên xem bảng tổng kết tuần
def summary_view (request,classroom):
    classroom = get_object_or_404(Classroom, name=classroom)
    lesson = get_lessons_week(classroom=classroom)
    context = {
        'lessons':lesson,
        'classroom':classroom
    }
    return render(request, 'summary.html', context)

# Lấy những tết học trong tuần để hiển thị tại summary
def get_lessons_week(classroom):
    # Xác định ngày đầu tiên của tuần
    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    # Xác định ngày cuối cùng của tuần
    end_of_week = start_of_week + timedelta(days=6)
    # Truy vấn các tiết học thuộc classroom và trong khoảng thời gian từ start_of_week đến end_of_week
    lessons_week = Lessons.objects.filter(classroom=classroom, date_time__date__range=[start_of_week, end_of_week])
    return lessons_week


# Thêm điểm cho học sinh trong khi đang học ( đang lỗi )
def studentMark_inSubject(request,classroom,student):
    classroom = get_object_or_404(Classroom, name=classroom)
    period = get_period()
    student = get_object_or_404(Student, pk=student)
    if not period:
        messages.error(request, 'Lỗi: Bạn đang KHÔNG trong giờ dạy.')
    else:
        now_subject = get_subject(classroom=classroom, period= period)
        mark_record = Mark.objects.filter(student=student, subject=now_subject).first()
        context = {
            'student': student,
            'subject': now_subject,
            'mark_record': mark_record,
            'classroom':classroom
        }
    return render(request, 'details.html', context)



    
    
    