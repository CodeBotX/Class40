from django.db import models
from .models import *
from django.core.exceptions import ValidationError
from django.core.serializers.json import DjangoJSONEncoder 
from django.contrib.postgres.fields import ArrayField


# Môn Học
class Subject (models.Model):
    id = models.CharField(primary_key=True, max_length = 10)
    name = models.CharField(max_length = 100,blank=False, null=False) # cần đảm bảo bắt buôc phải có
    def __str__(self):
        return f"{self.id}-{self.name}"

# Lớp Học
class Classroom(models.Model):
    name = models.CharField(primary_key=True,max_length=10)
    manager = models.ForeignKey('app_User.Teacher', on_delete=models.CASCADE,related_name='classroom') # 1 lớp chỉ có 1 giáo viên và ngược lại 
    def __str__(self):
        return self.name

# Môn Học Thuộc Lớp Học
class ClassroomSubject(models.Model):
    classroom = models.ForeignKey(Classroom,on_delete=models.CASCADE,related_name='subjects')
    subject = models.ManyToManyField(Subject,blank=True)
    def __str__(self):
        return f"{self.classroom} - {self.subject}"

#  Học Sinh
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100,blank=False, null=False)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='student') # cho phép classroom truy vấn được các student của mình
    def __str__(self):
        return f"{self.name} - {self.id}" 


# Tiết Học
class LessonTime(models.Model):
    period = models.CharField(max_length=10, unique=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    def clean(self):
        # Kiểm tra xem start_time có trước end_time không
        if self.start_time >= self.end_time:
            raise ValidationError(('Thời Gian Bắt Đầu Phải Trước Thời Gian Kết Thúc'))

    def __str__(self):
        return f"{self.period}: {self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')}"


class DailySchedule(models.Model):
    DAY_CHOICES = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )
    day_of_week = models.IntegerField(choices=DAY_CHOICES,)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='daily_schedules')
    def __str__(self):
        return f"{self.classroom.name} - {self.day_of_week}"
    def get_dayofweek(self):
        return f"{self.day_of_week}"

class ScheduleEntry(models.Model):
    daily_schedule = models.ForeignKey(DailySchedule, on_delete=models.CASCADE, related_name='schedule_entries')
    period = models.OneToOneField(LessonTime, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        ordering = ['period__start_time']  # Sắp xếp theo thời gian bắt đầu

    # def __str__(self):
    #     return f"{self.daily_schedule.classroom.name} - {self.get_day_display()} - Tiết {self.period.period}: {self.subject.name} ({self.period.start_time.strftime('%H:%M')} - {self.period.end_time.strftime('%H:%M')})"

# Năm học
class SchoolYear(models.Model):
    name = models.CharField(max_length=9)
    def validate_school_year_format(self):
        # Kiểm tra định dạng của 'name' để đảm bảo nó phù hợp với "YYYY-YYYY"
        if len(self.name) != 9 or self.name[4] != '-':
            return False
        start_year, end_year = self.name.split('-')
        if not (start_year.isdigit() and end_year.isdigit()):
            return False
        if int(end_year) - int(start_year) != 1:
            return False
        return True
    def save(self, *args, **kwargs):
        # Kiểm tra định dạng của 'name' trước khi lưu
        if not self.validate_school_year_format():
            raise ValidationError("'YYYY-YYYY'")
        super().save(*args, **kwargs)

# kì học
class Semester(models.Model):
    name = models.CharField(max_length=30)
    school_year = models.ForeignKey(SchoolYear,on_delete=models.CASCADE, related_name='schoolyear')

# Bảng Điểm 
class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='student')
    subject= models.ForeignKey(Subject, on_delete=models.CASCADE)
    scores = ArrayField(models.FloatField(), blank=True, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)  
    # def clean(self): 
    #     if self.subject not in self.student.classroom.subjects.all():
    #         raise ValidationError("Học sinh KHÔNG học môn học này.")
    
    
    # def add_mark(self, mark):
    #     if not (0 <= mark <= 10):
    #         raise ValidationError("Điểm không hợp lệ. Điểm phải nằm trong khoảng [0, 10].")
        
    #     # Lấy danh sách điểm hiện tại (hoặc khởi tạo một danh sách trống nếu chưa có điểm nào)
    #         current_scores = self.scores or []

    #     # Thêm điểm mới vào danh sách
    #         current_scores.append(mark)

    #     # Cập nhật trường scores với danh sách mới
    #         self.scores = current_scores
    #         self.save()
    #     return True
    
