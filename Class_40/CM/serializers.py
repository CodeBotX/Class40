# Lấy dữ liệu từ models chuyển về json và trả về cho client
# Nhận dữ liệu ở client ở dạng json và chuyển về object ( models )


from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'