from django.contrib import admin
from .models import *
from django.http import *



@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'first_name', 'last_name', 'department')
    search_fields = ('emp_id', 'first_name', 'last_name', 'department')

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'description')
    search_fields = ('job_id', 'description')

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('mach_id', 'description')
    search_fields = ('mach_id', 'description')

@admin.register(TimePunch)
class ClockInOutAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'job_id', 'mach_id', 'punch_in', 'punch_out', 'active', 'time')
    list_filter = ('active',)
    search_fields = ('emp_id', 'job_id', 'mach_id')