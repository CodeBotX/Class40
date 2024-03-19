
from django.urls import path,include, re_path
from rest_framework.routers import DefaultRouter
from .views import DailyScheduleViewSet
from .views import add_schedule
router = DefaultRouter()
router.register(r'daily-schedules', DailyScheduleViewSet)
from . import views

urlpatterns = [  
    path('api/', include(router.urls)),
    path('', views.school_view, name='School'),
    path('addsubject/', views.add_subject, name='add_subject'),
    path('addclassroom/', views.add_classroom, name='add_classroom'),
    path('addlessontime/', views.add_lesson_time, name='add_lesson_time'),
    path('addstudent/', views.add_student, name='add_student'),
    path('addtimetable/', views.add_schedule, name='add_timetable'),
]
