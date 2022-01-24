from cProfile import label
from socket import fromshare
from django import forms
from .models import regFORM

class regfrom(forms.ModelForm):
    class Meta:
        model = regFORM
        fields=['name','phoneno','email','dob']
        labels={"dob":"DOB(yyyy-mm-dd)"}