from django.contrib import admin
from .models import *



admin.site.register(Student)
admin.site.register(Lessons)
admin.site.register(Mark)


class SeatAdmin(admin.ModelAdmin):
    list_display = ('classroom', 'row', 'column', 'student')
    list_filter = ('classroom', 'column', 'row')  
admin.site.register(Seat, SeatAdmin)