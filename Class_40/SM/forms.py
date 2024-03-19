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

class ScheduleForm(forms.Form):
    day_of_week = forms.ChoiceField(choices=DailySchedule.DAY_CHOICES)
    classroom = forms.ModelChoiceField(queryset=Classroom.objects.all())
    period = forms.ModelChoiceField(queryset=LessonTime.objects.all())
    subject = forms.ModelChoiceField(queryset=Subject.objects.all())

    def save(self):
        daily_schedule = DailySchedule.objects.create(
            day_of_week=self.cleaned_data['day_of_week'],
            classroom=self.cleaned_data['classroom']
        )
        ScheduleEntry.objects.create(
            daily_schedule=daily_schedule,
            period=self.cleaned_data['period'],
            subject=self.cleaned_data['subject']
        )
