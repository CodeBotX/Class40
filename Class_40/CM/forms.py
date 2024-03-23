
'''
Form add lesson
Form add điểm
Form lựa chọn lớp học

'''

from django import forms
from django.core.exceptions import ValidationError
from .models import *
from SM.models import Mark

# 
class MarkForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        student = kwargs.pop('student', None)
        subject = kwargs.pop('subject', None)
        super(MarkForm, self).__init__(*args, **kwargs)
        if student:
            self.fields['student'].initial = student
            self.fields['student'].widget = forms.HiddenInput()
        if subject:
            self.fields['subject'].initial = subject
            self.fields['subject'].widget = forms.HiddenInput()

    class Meta:
        model = Mark
        fields = ['scores']

# Form chọn lớp học
class ClassroomSelectionForm(forms.Form):
    classroom = forms.ModelChoiceField(queryset=Classroom.objects.all(), empty_label=None, label='Select_Classroom')
    
# Form add lession

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lessons
        fields = ['name', 'counter', 'comment', 'grade']

    def __init__(self, *args, **kwargs):
        self.teacher = kwargs.pop('teacher', None)
        super(LessonForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(LessonForm, self).save(commit=False)
        instance.teacher = self.teacher
        if commit:
            instance.save()
        return instance

# class MarkForm(forms.ModelForm):
#     class Meta:
#         fields = 