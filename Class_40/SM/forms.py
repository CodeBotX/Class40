from django import forms
from .models import *

# FILE FORM 

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['id', 'name']

class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ['name', 'manager']

class LessonTimeForm(forms.ModelForm):
    class Meta:
        model = LessonTime
        fields = ['period', 'start_time', 'end_time']

        
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id', 'name', 'classroom']

class ClassoomSubjectForm(forms.ModelForm):
    models = ClassroomSubject
    fields =['classroom','subject']

class TableScheduleForm(forms.ModelForm):
    models = TableSchedule
    fields =['classroom','dayofweek','period','subject']
    
    