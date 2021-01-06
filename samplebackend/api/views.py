from django.shortcuts import render
from django.http import HttpResponse
import time
import datetime

# Create your views here.
## put code that could responsible for rendering views and api end points

def main(request):
    datetime_dt = datetime.datetime.today() # 獲得當地時間
    dateTimeFormat = datetime_dt.strftime("%Y/%m/%d %H:%M:%S")  # 格式化日期(最小單位到秒)
    # time_delta = datetime.timedelta(hours=3) #時差
    # new_dt = datetime_dt + time_delta #本地時間加3小時
    # datetime_format = new_dt.strftime("%Y/%m/%d %H:%M:%S")  # 格式化日期(最小單位到秒)
    return HttpResponse(f"Hello , time is {dateTimeFormat}!")

from rest_framework import generics
from .serializers import RoomSerializers
from .models import Room

class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers
    
