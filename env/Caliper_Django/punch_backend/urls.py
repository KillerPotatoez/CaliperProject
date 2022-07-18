from django.urls import path, include
import django.contrib.auth
from django.contrib import admin
from . import views
admin.autodiscover()

urlpatterns = [
     path('', views.clockin, name='index'),
     path('clockIn/', views.clockin, name='clockin'),
     path('clockOut/', views.clockout, name='clockout'),
     path('admin/', admin.site.urls),
]