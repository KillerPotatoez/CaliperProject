from .models import *
from .serializers import PunchSerializer
from rest_framework.generics import ListAPIView,CreateAPIView, UpdateAPIView
from datetime import *
from django.utils import formats
from django.template import Context, loader
from django.template.context_processors import csrf
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import RequestContext
date_punched = datetime.now()
formatted_datetime = formats.date_format(date_punched, "SHORT_DATETIME_FORMAT")

class GetPunch(ListAPIView):
    queryset=TimePunch.objects.all()
    serializer_class = PunchSerializer

class AddPunch(CreateAPIView):
    queryset=TimePunch.objects.all()
    serializer_class = PunchSerializer

def create(self, validated_data):
    obj, created = TimePunch.objects.update_or_create(
        emp_id=validated_data.get('emp_id'),
        active=0
    )

def clockin(request):
        if request.method == 'POST':
                form = IndexForm( request.POST )
                if form.is_valid():
                        instance = form.save( commit=False )
                        employee = Employee.objects.get( employee_number=instance.employee_number )
                        job = Job.objects.get( job_number=instance.job_number )
                        shift = ClockEvent()
                        shift.clockIn(employee, job)
                        return render(request, 'punchclock/clockin.html', { 'first_name':employee.first_name, 'last_name':employee.last_name, 'in_time':shift.in_time} )
                else:
                        to_add = { }
                        to_add.update( { 'form': form } )
                        print ('Error! user didnt enter a field and hit clock in')
                        return render(request, '404.html', to_add )

        else:
                to_add = { }
                to_add.update( csrf( request ) )
                form = IndexForm()
                to_add.update( { 'form': form } )
                return render(request, 'punchclock/index.html', to_add )

def clockout(request):
        if request.method == 'POST':
                form = IndexForm( request.POST )
                if form.is_valid():
                        instance = form.save( commit=False )
                        Employee = Employee.objects.get( employee_number=instance.employee_number )
                        Job = Job.objects.get( job_number=instance.job_number )
                        shift = ClockEvent()
                        shift.clockOut( Employee, Job )
                        return render(request, 'punchclock/clockout.html', {'first_name': Employee.first_name, 'last_name': Employee.last_name, 'out_time':shift.out_time} )
                else:
                        print ('Error! User didnt enter a field and hit clock out')
                        to_add = { }
                        to_add.update( { 'form': form } )
                        to_add.update( csrf( request ) )
                        return render(request, '404.html', to_add )


