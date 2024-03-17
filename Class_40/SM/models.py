from django.db import models
from .models import *
from django.core.exceptions import ValidationError




class Subject (models.Model):
    id = models.CharField(primary_key=True, max_length = 10)
    name = models.CharField(max_length = 100,blank=False, null=False) # cần đảm bảo bắt buôc phải có
    def __str__(self):
        return f"{self.id}-{self.name}"

class Classroom(models.Model):
    name = models.CharField(primary_key=True,max_length=100)
    manager = models.ForeignKey('app_User.Teacher', on_delete=models.CASCADE,related_name='classroom') # 1 lớp chỉ có 1 giáo viên và ngược lại 
    subjects = models.ManyToManyField(Subject,blank=True, related_name='classrooms') # choise từ subject

    def __str__(self):
        return self.name


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

class ScheduleEntry(models.Model):
    daily_schedule = models.ForeignKey(DailySchedule, on_delete=models.CASCADE, related_name='schedule_entries')
    period = models.ForeignKey(LessonTime, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        ordering = ['period__start_time']  # Sắp xếp theo thời gian bắt đầu

    def __str__(self):
        return f"{self.daily_schedule.classroom.name} - {self.get_day_display()} - Tiết {self.period.period}: {self.subject.name} ({self.period.start_time.strftime('%H:%M')} - {self.period.end_time.strftime('%H:%M')})"
    
    