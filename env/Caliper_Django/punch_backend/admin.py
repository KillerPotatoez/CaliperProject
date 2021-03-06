from django.contrib import admin
from punchclock.models import *
from django.conf.urls import patterns, include, url
from django.http import *
from django.template import RequestContext, loader
from django.core.exceptions import PermissionDenied
from django.utils.encoding import force_unicode
from django.contrib.admin import helpers
from django.template.response import TemplateResponse


admin.site.register(Account)
admin.site.register(Department)

class UserAdmin(admin.ModelAdmin):
        fields = ['first_name', 'last_name', 'number', 'start_date', 'amount_paid', 'department', 'account', 'active' ]

        def get_urls(self):
                urls = super(UserAdmin, self).get_urls()
                my_urls = patterns('',
                        #(r'^generate_timecards/$', self.admin_site.admin_view(self.generate_timecards)),
                        (r'^change_hours/$', self.admin_site.admin_view(self.change_hours))
                )
                return my_urls + urls

        def generate_timecards(self, request, queryset):
                if request.POST.get('post'):
                        if perms_needed:
                                raise PermissionDenied
                        n = queryset.count()
                        if n:
                                for obj in queryset:
                                        obj_display = force_unicode(obj)
                else:
                        context = {
                                'title' : ("Generate timecards?"),
                                'queryset' : queryset,
                                'action_checkbox_name' : helpers.ACTION_CHECKBOX_NAME,
                        }
                        return TemplateResponse(request, 'admin/generate_timecards.html',context, current_app=self.admin_site.name)
#       actions = [generate_timecards]

        def change_hours(self, request, queryset):
                if request.POST.get('post'):
                        if perms_needed:
                                raise PermissionDenied
                        n = queryset.count()
                        if n:
                                for obj in queryset:
                                        obj_display = force_unicode(obj)
                else:
                        context = {
                                'title' : ("Change hours?"),
                                'queryset' : queryset,
                                'action_checkbox_name' : helpers.ACTION_CHECKBOX_NAME,
                        }

                        return TemplateResponse(request, 'admin/change_hours.html',context, current_app=self.admin_site.name)

        actions = [change_hours, generate_timecards]

admin.site.register(User, UserAdmin)