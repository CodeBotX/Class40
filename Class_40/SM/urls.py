
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import DailyScheduleViewSet
from .views import add_schedule
router = DefaultRouter()
router.register(r'daily-schedules', DailyScheduleViewSet)
from . import views

urlpatterns = [
    # path('addtimetable/', views.add_timetable, name='AddTiemTable'),   
    path('api/', include(router.urls)),
    # path('addschedule/', add_schedule, name='add_schedule'),
]
