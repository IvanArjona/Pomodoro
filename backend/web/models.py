from django.db import models


class TimerType(models.Model):
    name = models.CharField(max_length=32)
    work = models.BooleanField()


class Timer(models.Model):
    task = models.CharField(max_length=128)
    duration = models.DurationField()
    start = models.DateTimeField(auto_now=True)
    end = models.DateTimeField()
    timer_type = models.ForeignKey(TimerType, on_delete=models.CASCADE)

