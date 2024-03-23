from django.db import models
from django.core.exceptions import ValidationError
from SM.models import Subject
from SM.models import Student
from SM.models import Classroom
from django.db.models.signals import post_save
from django.dispatch import receiver

  

# Tiết học
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

        
class Seat(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='seats')
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True,related_name='seat')
    row = models.PositiveIntegerField()
    column = models.PositiveIntegerField()
    def is_empty(self):
        # Kiểm tra xem chỗ ngồi có trống hay không (chưa được sử dụng bởi học sinh).
        return self.student is None
    def assign_student(self, student):
        # Kiểm tra xem học sinh thuộc lớp học của bạn hay không
        if student.classroom == self.classroom:
            self.student = student
            self.save()
            print(f"Học sinh {student.name} đã được gán vào chỗ ngồi tại hàng {self.row}, cột {self.column}.")
        else:
            print(f"Học sinh {student.name} không thuộc lớp học của bạn.")

@receiver(post_save, sender=Classroom)
def create_seats(sender, instance, created, **kwargs):
    if created:
        rows = 5
        columns = 8
        for row in range(1, rows + 1):
            for column in range(1, columns + 1):
                seat_number = (row - 1) * columns + column
                Seat.objects.create(classroom=instance, row=row, column=column)

