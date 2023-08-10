from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from .models import TimePunch
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from .forms import *

def index(request):
    form = PunchIN()

    if request.method == 'POST':
        form = PunchIN(request.POST)
        if form.is_valid():
            emp_id = form.cleaned_data['emp_id']
            job_id = form.cleaned_data['job_id']
            mach_id = form.cleaned_data['mach_id']

            # Perform clock in action and handle the logic
            response = perform_clock_in(emp_id, job_id, mach_id)
            return JsonResponse(response)

    return render(request, 'index.html', {'form': form})

def perform_clock_in(emp_id, job_id, mach_id):
    response = {}
    existing_session = TimePunch.objects.filter(emp_id=emp_id, active=True).first()
    if existing_session:
        existing_session.punch_out = timezone.now()
        existing_session.active = False
        existing_session.time = (existing_session.punch_out - existing_session.punch_in).total_seconds() / 3600
        existing_session.save()
        response['message'] = 'Clock out successful'
    else:
        new_session = TimePunch(emp_id=emp_id, job_id=job_id, mach_id=mach_id)
        new_session.punch_in = timezone.now()
        new_session.active = True
        new_session.save()
        response['message'] = 'Clock in successful'

    return response
# def perform_clock_in(request, emp_id, job_id, mach_id):
#     if request.method == 'POST':
#         emp_id = request.POST.get('emp_id')
#         job_id = request.POST.get('job_id')
#         mach_id = request.POST.get('mach_id')

#         existing_session = TimePunch.objects.filter(emp_id=emp_id, job_id=job_id, mach_id=mach_id, active=True).first()
#         if existing_session:
#             existing_session.punch_out = timezone.now()
#             existing_session.active = False
#             existing_session.time = existing_session.punch_out - existing_session.punch_in
#             existing_session.save()
#             return JsonResponse({'message': 'Clock out successful'})
        
#         new_session = TimePunch(emp_id=emp_id, job_id=job_id, mach_id=mach_id)
#         new_session.punch_in = timezone.now()
#         new_session.active = True
#         new_session.save()

#         return JsonResponse({'message': 'Clock in successful'})

#     return JsonResponse({'message': 'Invalid request'}, status=400)


# def update_job_station(request):
#     emp_id = request.POST.get('emp_id')
#     job_id = request.POST.get('job_id')
#     station_id = request.POST.get('mach_id')

#     # Find the active clock-in session for the employee
#     session = get_object_or_404(TimePunch, emp_id=emp_id, active=True)

#     # Update job_id and station_id
#     session.job_id = job_id
#     session.station_id = station_id
#     session.save()

#     return JsonResponse({'message': 'Job and Station updated successfully'})




