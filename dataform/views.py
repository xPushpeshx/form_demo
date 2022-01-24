from django.shortcuts import render
from .forms import regfrom
from .models import regFORM 
import csv
from django.http import HttpResponse

def home(request):
    if request.method=='POST':
        fm=regfrom(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            dob=fm.cleaned_data['dob']
            pn=fm.cleaned_data['phoneno']
            reg=regFORM(name=nm,email=em,dob=dob,phoneno=pn)
            reg.save()
        stud=regFORM.objects.order_by('dob')  
        return render(request,'data.html',{'stu':stud})
    else:
        fm=regfrom()
    
    return render(request,'index.html',{'form':fm})

def data(request):
    stud=regFORM.objects.order_by('dob')
    return render(request,'data.html',{'stu':stud})

def getfile(request):
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    data = regFORM.objects.order_by('dob') 
    writer = csv.writer(response)  
    for ch in data:  
        writer.writerow([ch.name,ch.phoneno,ch.email,ch.dob])  
    return response 