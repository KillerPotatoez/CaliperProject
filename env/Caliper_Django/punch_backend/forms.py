from django import forms 

class PunchIN(forms.Form):
    emp_id = forms.CharField(max_length=25,required=True)
    job_id = forms.CharField(max_length=25,required=True)
    mach_id = forms.CharField(max_length=25,required=True)