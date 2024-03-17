from django import forms


# FILE FORM 
from .models import DailySchedule

class DailyScheduleForm(forms.ModelForm):
    class Meta:
        model = DailySchedule
        fields = ['day_of_week', 'classroom']
