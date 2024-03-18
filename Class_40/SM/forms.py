from django import forms
from .models import *
from CM.models import Student

# FILE FORM 
from .models import DailySchedule

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['id', 'name']

class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ['name', 'manager', 'subjects']

class LessonTimeForm(forms.ModelForm):
    class Meta:
        model = LessonTime
        fields = ['period', 'start_time', 'end_time']

class DailyScheduleForm(forms.ModelForm):
    class Meta:
        model = DailySchedule
        fields = ['day_of_week', 'classroom']
        
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'classroom']
