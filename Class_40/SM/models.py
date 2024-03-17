from django.db import models
from .models import *
from CM.models import Subject as CM_Subject
from CM.models import Classroom as CM_Classroom
from django.core.exceptions import ValidationError



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
    classroom = models.ForeignKey(CM_Classroom, on_delete=models.CASCADE, related_name='daily_schedules')
    def __str__(self):
        return f"{self.classroom.name} - {self.day_of_week}"

class ScheduleEntry(models.Model):
    daily_schedule = models.ForeignKey(DailySchedule, on_delete=models.CASCADE, related_name='schedule_entries')
    period = models.ForeignKey(LessonTime, on_delete=models.CASCADE)
    subject = models.ForeignKey(CM_Subject, on_delete=models.CASCADE)

    class Meta:
        ordering = ['period__start_time']  # Sắp xếp theo thời gian bắt đầu

    def __str__(self):
        return f"{self.daily_schedule.classroom.name} - {self.get_day_display()} - Tiết {self.period.period}: {self.subject.name} ({self.period.start_time.strftime('%H:%M')} - {self.period.end_time.strftime('%H:%M')})"
    
    