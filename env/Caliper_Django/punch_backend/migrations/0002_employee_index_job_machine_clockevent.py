# Generated by Django 4.0.5 on 2022-07-18 00:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('punch_backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_number', models.IntegerField(max_length=8)),
                ('first_name', models.CharField(max_length=512)),
                ('last_name', models.CharField(max_length=512)),
                ('department', models.CharField(max_length=512)),
                ('pay_rate', models.FloatField()),
                ('phone_number', models.CharField(max_length=512)),
                ('alt_phone_number', models.CharField(blank=True, max_length=512, null=True)),
                ('address_id', models.IntegerField(max_length=8)),
                ('drivers_license', models.IntegerField(max_length=15)),
                ('birth_date', models.DateField()),
                ('ssn', models.CharField(max_length=512)),
                ('coverage_id', models.IntegerField(blank=True, max_length=8, null=True)),
                ('gender', models.CharField(max_length=12)),
                ('start_date', models.DateField(default=datetime.datetime(2022, 7, 17, 19, 3, 11, 831806))),
                ('end_date', models.DateField(blank=True, null=True)),
                ('emergency_contact', models.CharField(max_length=512)),
                ('emergency_phone_number', models.CharField(max_length=512)),
                ('status', models.IntegerField(default=1)),
                ('in_time', models.TimeField()),
                ('is_in', models.BooleanField(verbose_name=False)),
                ('out_time', models.TimeField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_number', models.IntegerField(max_length=8)),
                ('job_number', models.CharField(max_length=20)),
                ('machine_number', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_number', models.IntegerField(max_length=8)),
                ('description', models.CharField(max_length=512)),
                ('start_date', models.DateField(default=datetime.datetime(2022, 7, 17, 19, 3, 11, 830806))),
                ('end_date', models.DateField(blank=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('quoted_hours', models.FloatField(blank=True, null=True)),
                ('actual_hours', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_number', models.IntegerField(max_length=20)),
                ('description', models.CharField(max_length=512)),
                ('regular_rate', models.FloatField()),
                ('rush_rate', models.FloatField()),
                ('p_rate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ClockEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='punch_backend.employee')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='punch_backend.job')),
                ('machine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='punch_backend.machine')),
            ],
        ),
    ]
