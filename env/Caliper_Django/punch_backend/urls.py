from django.conf.urls import patterns, include, url
import django.contrib.auth
from django.contrib import admin

urlpatterns = patterns('',
     url(r'^$', 'views.clockin', name='index'),
     url(r'^clockIn/$', 'views.clockin', name='clockin'),
     url(r'^clockOut/$', 'views.clockout', name='clockout'),
)