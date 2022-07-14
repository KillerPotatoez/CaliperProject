from rest_framework import serializers
from .models import TimePunch

class PunchSerializer(serializers.ModelSerializer):
    class Meta:
        fields =(
            'id',
	        'emp_id',
            'job_id',
	        'mach_id',
	        'punch_in',
	        'punch_out',
            'active',
	        'time',
            )
        model = TimePunch