from django.db import models
from django.core.exceptions import ValidationError
from django.core.serializers.json import DjangoJSONEncoder 
import json


# blank=False đảm bảo rằng trường không được để trống khi biểu mẫu được gửi (liên quan đến xác thực dữ liệu biểu mẫu).
# null=False đảm bảo rằng cơ sở dữ liệu sẽ không lưu giá trị NULL cho trường này (liên quan đến cơ sở dữ liệu).

# Create your models here.


class Subject (models.Model):
    id = models.CharField(primary_key=True, max_length = 10)
    name = models.CharField(max_length = 100,blank=False, null=False) # cần đảm bảo bắt buôc phải có
    def __str__(self):
        return f"{self.id}-{self.name}"

class Classroom(models.Model):
    name = models.CharField(primary_key=True,max_length=100)
    manager = models.ForeignKey('app_User.Teacher', on_delete=models.CASCADE,related_name='classroom') # 1 lớp chỉ có 1 giáo viên và ngược lại 
    subjects = models.ManyToManyField(Subject,blank=True, related_name='classrooms') # choise từ subject

    def __str__(self):
        return self.name
    

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=100,blank=False, null=False)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='student') # cho phép classroom truy vấn được các student của mình
    def __str__(self):
        return f"{self.full_name} - {self.id}" 

class Lessons (models.Model):
    name = models.CharField(max_length=150)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE) 
    classroom = models.ForeignKey(Classroom,on_delete=models.CASCADE)
    teacher = models.ForeignKey('app_User.Teacher', on_delete=models.CASCADE)
    counter = models.PositiveIntegerField(default=1)  # Thêm trường counter (đếm số tiết)
    comment = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    grades = (
        ('T', 'Tốt'),
        ('K', 'Khá'),
        ('TB', 'Trung Bình'),
        ('Y', 'Yếu'),
    )
    grade = models.CharField(max_length=2, choices=grades, default='TB')

    def __str__(self):
        return f"{self.name} - {self.classroom}"
    
    def clean(self):
        if not self.grade:
            raise ValidationError("Bạn chưa chấm điểm bài học.")

    def save(self, *args, **kwargs):
        if not self.pk:  # Nếu đây là một tiết học mới
            last_lesson = Lessons.objects.filter(classroom=self.classroom, subject=self.subject).order_by('-counter').first()
            if last_lesson:
                self.counter = last_lesson.counter + 1
        super().save(*args, **kwargs)


class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject= models.ForeignKey(Subject, on_delete=models.CASCADE)
    Mark = models.JSONField(encoder=DjangoJSONEncoder, default=list)
    def clean(self):
        if self.subject not in self.student.classroom.subjects.all():
            raise ValidationError("The selected subject is not one of the subjects that the student is studying.")