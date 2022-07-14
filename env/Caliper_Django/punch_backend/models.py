from bdb import effective
from django.db import models
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.forms import ModelForm
from django.shortcuts import render_to_response
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

    def __str__(self):
        return self.name


class Job(models.Model):
    number = models.IntegerField(max_length=8)
    description = models.CharField(max_length=512)
    start_date = models.DateField(default=datetime.now())
    end_date = models.DateField(blank=True,null=True)
    due_date = models.DateField(blank=True,null=True)
    quoted_hours = models.FloatField(blank=True,null=True)
    actual_hours = models.FloatField(blank=True,null=True)
    
    def __str__(self):
        return self.name

class Machine(models.Model):
    number = models.IntegerField(max_length=8)
    description = models.CharField(max_length=512)
    regular_rate = models.FloatField()
    rush_rate = models.FloatField()
    p_rate = models.FloatField()

    def __str__(self):
            return self.name

class Employee(models.Model):
    number = models.IntegerField(max_length=8)
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

    in_time = models.TimeField()
    is_in = models.BooleanField(False)
    out_time = models.TimeField()
    active = models.BooleanField(default = True)

    def __str__(self):
        return str(self.last_name) + ', ' + str(self.first_name) + ' : ' + str(self.number)

class ClockEvent(models.Model):
	employee = models.ForeignKey(Employee)
	job = models.ForeignKey(Job)
	machine = models.ForeignKey(Machine, null=True, blank=True)

	def clockIn(self, employee, job):
		self.Employee = employee
		self.is_in = employee.is_in
		self.in_time = employee.in_time
		self.out_time = employee.out_time

		self.employee = employee

		if self.is_in is True:
			print ("Error! is_in is True. User is already clocked in!")
			return

		self.job = job
		self.in_time = user.in_time = datetime.now().replace(microsecond=0)
		self.is_in = user.is_in = True

		print ("self.in_time is...")
		print (self.in_time)

		print ("self.is_in is ...")
		print (self.is_in)

		self.save()
		return
		
	def clockOut(self, user, department):

		self.user = user
		self.is_in = user.is_in
		self.in_time = user.in_time
		self.out_time = user.out_time

		if self.is_in is False:
			print "Error! user is clocked out, is_in is False"
			return

		if self.in_time > self.out_time:
			print "Error! in_time is greater than out_time"
			return False

		self.department = department
		self.out_time = user.out_time = datetime.now().replace(microsecond=0)
		self.is_in = user.is_in = False

		print "self.out_time is.."
		print self.out_time

		print "self.is_in is..."
		print self.is_in

		print "self.in_time is..."
		print self.in_time
		#TODO in_time is NONE!!!!

		self.save()
		return