# Generated by Django 4.0.5 on 2022-07-18 03:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('punch_backend', '0011_alter_employee_start_date_alter_job_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2022, 7, 17, 22, 48, 30, 611326)),
        ),
        migrations.AlterField(
            model_name='job',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2022, 7, 17, 22, 48, 30, 611326)),
        ),
    ]
