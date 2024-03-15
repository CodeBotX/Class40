from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.classroom_view, name='Classroom'),
]
