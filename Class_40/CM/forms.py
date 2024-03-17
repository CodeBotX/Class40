
'''
Form add lesson
Form add điểm
Form lựa chọn lớp học

'''

from django import forms
from django.core.exceptions import ValidationError
from .models import *

# 
class MarkAddForm(forms.Form):
    mark = forms.IntegerField(label='Mark', min_value=0, max_value=10)  # Đặt giới hạn cho trường nhập liệu

    def clean_mark(self):
        mark = self.cleaned_data.get('mark')
        # Kiểm tra xem điểm có nằm trong khoảng từ 0 đến 10 hay không
        if mark <= 0 or mark >= 10:
            raise ValidationError('Điểm số phải nằm trong khoảng từ 0 đến 10.') 
        return mark

# Form chọn lớp học
class ClassroomSelectionForm(forms.Form):
    classroom = forms.ModelChoiceField(queryset=Classroom.objects.all(), empty_label=None, label='Select a Classroom')
    
# Form add lession

# 