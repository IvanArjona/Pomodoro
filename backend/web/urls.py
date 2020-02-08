from django.urls import path
from . import views


urlpatterns = [
    path('api/timers', views.timers, name='timers'),
]
