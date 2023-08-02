# Generated by Django 4.0.5 on 2022-07-18 02:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('punch_backend', '0005_alter_employee_is_in_alter_employee_start_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='is_in',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2022, 7, 17, 21, 29, 17, 271)),
        ),
        migrations.AlterField(
            model_name='job',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2022, 7, 17, 21, 29, 16, 999270)),
        ),
    ]
