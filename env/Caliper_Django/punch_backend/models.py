from bdb import effective
from django.db import models
from django.contrib import admin
from django.urls import re_path, include
from django.forms import ModelForm
from django.shortcuts import render
from datetime import *

class TimePunch(models.Model):
    emp_id = models.IntegerField()
    job_id = models.IntegerField()
    mach_id = models.IntegerField()
    punch_in = models.DateTimeField(
        blank=True,
        null=True
    )
    punch_out = models.DateTimeField(
        blank=True,
        null=True
    )
    active = models.IntegerField(default=0)
    time = models.FloatField(
        blank=True,
        null=True
    )

    def __unicode__(self):
        return self.emp_id


class Job(models.Model):
    job_number = models.IntegerField(max_length=8)
    description = models.CharField(max_length=512)
    start_date = models.DateField(default=datetime.now())
    end_date = models.DateField(blank=True,null=True)
    due_date = models.DateField(blank=True,null=True)
    quoted_hours = models.FloatField(blank=True,null=True)
    actual_hours = models.FloatField(blank=True,null=True)
    
    def __unicode__(self):
        return self.job_number

class Machine(models.Model):
    machine_number = models.IntegerField(max_length=20)
    description = models.CharField(max_length=512)
    regular_rate = models.FloatField()
    rush_rate = models.FloatField()
    p_rate = models.FloatField()

    def __unicode__(self):
            return self.machine_number

class Employee(models.Model):
    employee_number = models.IntegerField(max_length=8)
    first_name = models.CharField(max_length=512)
    last_name = models.CharField(max_length=512)
    department = models.CharField(max_length=512)
    pay_rate = models.FloatField()
    phone_number = models.CharField(max_length=512)
    alt_phone_number = models.CharField(max_length=512, blank=True,null=True)
    address_id = models.IntegerField(max_length=8)
    drivers_license = models.IntegerField(max_length=15)
    birth_date = models.DateField()
    ssn = models.CharField(max_length=512)
    coverage_id = models.IntegerField(max_length=8,blank=True,null=True)
    gender = models.CharField(max_length=12)
    start_date = models.DateField(default=datetime.now())
    end_date = models.DateField(blank=True,null=True)
    emergency_contact = models.CharField(max_length=512)
    emergency_phone_number = models.CharField(max_length=512)
    status = models.IntegerField(default=1)

    in_time = models.TimeField(blank=True,null=True)
    is_in = models.BooleanField(default=False,blank=True,null=True)
    out_time = models.TimeField(blank=True,null=True)
    active = models.BooleanField(default = True)

    def __unicode__(self):
        return str(self.last_name) + ', ' + str(self.first_name) + ' : ' + str(self.employee_number)

class ClockEvent(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE , null=True, blank=True)
    
    def clockIn(self, employee, job):
        self.employee = employee
        self.is_in = employee.is_in
        self.in_time = employee.in_time
        self.out_time = employee.out_time
        
        if self.is_in is True:
            print ("Error! is_in is True. User is already clocked in!")
            return

        self.job = job
        self.in_time = employee.in_time = datetime.now().replace(microsecond=0)
        self.is_in = employee.is_in = True
        
        print ("self.in_time is...")
        print (self.in_time)
        
        print ("self.is_in is ...")
        print (self.is_in)
        self.save()
        return
	    
    def clockOut(self, employee, job):
        
        self.employee = employee
        self.is_in = employee.is_in
        self.in_time = employee.in_time
        self.out_time = employee.out_time
        
        if self.is_in is False:
            print ("Error! employee is clocked out, is_in is False")
            return

        if self.in_time > self.out_time:
            print ("Error! in_time is greater than out_time")
            return False
        
        self.job = job
        self.out_time = employee.out_time = datetime.now().replace(microsecond=0)
        self.is_in = employee.is_in = False
        
        print ("self.out_time is..")
        print (self.out_time)
        
        print ("self.is_in is...")
        print (self.is_in)

        print ("self.in_time is...")
        print (self.in_time)
        #TODO in_time is NONE!!!!
        
        self.save()
        return

class Index(models.Model):
    employee_number = models.IntegerField(max_length=8)
    job_number = models.CharField(max_length=20)
    machine_number = models.IntegerField(max_length=20)

class IndexForm(ModelForm):
        class Meta:
                model = Index
                fields = ['employee_number', 'job_number', 'machine_number']