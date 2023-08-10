from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
     path('', views.index, name='index'),
     path('perform_clock_in/', views.perform_clock_in, name='perform_clock_in'),
     # path('^clockOut/$', views.clockout, name='clockout'),
]