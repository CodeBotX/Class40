from rest_framework import serializers
from .models import DailySchedule

class DailyScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailySchedule
        fields = '__all__'