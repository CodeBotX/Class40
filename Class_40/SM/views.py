from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from rest_framework import viewsets
from .models import DailySchedule
from .serializers import DailyScheduleSerializer




class DailyScheduleViewSet(viewsets.ModelViewSet):
    queryset = DailySchedule.objects.all()
    serializer_class = DailyScheduleSerializer

# xử lý người dùng add thời Khóa biểu 
from .forms import DailyScheduleForm
from .models import DailySchedule
def add_schedule(request):
    if request.method == 'POST':
        form = DailyScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    else:
        form = DailyScheduleForm()
    return render(request, 'add_schedule.html', {'form': form})