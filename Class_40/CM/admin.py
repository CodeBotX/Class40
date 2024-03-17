from django.contrib import admin
from .models import *
# Register your models here.

# Register your models here.
# admin.site.register(Subject)
# admin.site.register(Classroom)
admin.site.register(Student)
admin.site.register(Lessons)
admin.site.register(Mark)


# @admin.register(Classroom)
# class ClassroomAdmin(admin.ModelAdmin):
#     list_display = ['name', 'manager']
#     filter_horizontal = ('subjects',)  # Cho phép dễ dàng quản lý mối quan hệ ManyToMany trong giao diện admin

# @admin.register(Subject)
# class SubjectAdmin(admin.ModelAdmin):
#     list_display = ['name']  # Giả sử rằng Subject có trường 'name'