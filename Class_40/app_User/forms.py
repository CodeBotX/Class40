from django import forms
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate




class SignUpForm(forms.Form):
    email = forms.EmailField(label='Email',widget=forms.EmailInput)
    id = forms.CharField(label="ID",widget=forms.NumberInput)
    first_name = forms.CharField(label='FirstName')
    last_name = forms.CharField(label ="LastName")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation" ,widget=forms.PasswordInput)
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1==password2 and password1:
                return password2
        raise forms.ValidationError('Mật Khẩu không Hợp Lệ')
    def clean_email(self):
        email = self.cleaned_data.get('email')
        User = get_user_model()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Tài khoản với địa chỉ email này đã tồn tại.")
        return email
    def save(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password1']
        id = self.cleaned_data['id']
        last_name = self.cleaned_data['last_name']
        first_name = self.cleaned_data['first_name']
        # Tạo đối tượng Teacher mới
        teacher = Teacher(email=email, id=id,first_name=first_name,last_name=last_name)
        teacher.set_password(password)  # Mã hóa mật khẩu
        teacher.save()  # Lưu teacher vào cơ sở dữ liệu
        return teacher



        

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Email hoặc mật khẩu không đúng. Vui lòng thử lại.")

        return cleaned_data

    def get_user(self):
        return Teacher.objects.get(email=self.cleaned_data['email'])


class StudentLookupForm(forms.Form):
    student_id = forms.IntegerField(label='Student ID', required=True)