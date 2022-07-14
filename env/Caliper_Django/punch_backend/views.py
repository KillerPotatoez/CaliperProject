from .models import TimePunch
from .serializers import PunchSerializer
from rest_framework.generics import ListAPIView,CreateAPIView, UpdateAPIView
from datetime import datetime
from django.utils import formats
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


