from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name='Home'),
    path('<str:classroom>/', views.classroom, name= 'classroom'),
    
]

