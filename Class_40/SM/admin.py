from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(LessonTime)
admin.site.register(DailySchedule)
admin.site.register(ScheduleEntry)