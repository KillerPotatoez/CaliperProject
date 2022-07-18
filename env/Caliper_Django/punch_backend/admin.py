from django.contrib import admin
from punch_backend.models import *
from django.urls import re_path, include
from django.http import *
from django.template import RequestContext, loader
from django.core.exceptions import PermissionDenied
from django.contrib.admin import helpers
from django.template.response import TemplateResponse


admin.site.register(Job)
admin.site.register(Machine)

class UserAdmin(admin.ModelAdmin):
        fields = ['first_name', 'last_name', 'department', 'pay_rate', 'phone_number', 'alt_phone_number', 'address_id', 'drivers_license', 'birth_date', 'ssn', 'coverage_id', 'gender','status', 'end_date', 'emergency_contact', 'emergency_phone_number', 'employee_number', 'start_date', 'active' ]

        def get_urls(self):
                urls = super(UserAdmin, self).get_urls()
                my_urls = [
                        #(r'^generate_timecards/$', self.admin_site.admin_view(self.generate_timecards)),
                        re_path(r'^change_hours/$', self.admin_site.admin_view(self.change_hours))
                ]
                return my_urls + urls

        def generate_timecards(self, request, queryset):
                        context = {
                                'title' : ("Generate timecards?"),
                                'queryset' : queryset,
                                'action_checkbox_name' : helpers.ACTION_CHECKBOX_NAME,
                        }
                        return TemplateResponse(request, 'admin/generate_timecards.html')
        #actions = [generate_timecards]

        def change_hours(self, request, queryset):
                        context = {
                                'title' : ("Change hours?"),
                                'queryset' : queryset,
                                'action_checkbox_name' : helpers.ACTION_CHECKBOX_NAME,
                        }

                        return TemplateResponse(request, 'admin/change_hours.html')
        actions = [change_hours, generate_timecards]

admin.site.register(Employee, UserAdmin)