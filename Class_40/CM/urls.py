
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name='Home'),
    path('<str:classroom>/', views.classroom, name= 'classroom'),
    path('<str:classroom>/summary/', views.summary_view, name= 'summary'), 
    path('<str:classroom>/<int:student>/', views.studentMark_inSubject, name= 'studentMark_inSubject'),

]

