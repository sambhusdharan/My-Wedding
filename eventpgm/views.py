from django.shortcuts import render
#from django.http import HttpResponse
from .models import *

# Create your views here.
def new_wedding(request):
    obj=wedding.objects.all()
    event=wedding_event.objects.all()
    stories=story.objects.all()
    return render(request,"index.html",{'results':obj,'event':event ,'story':stories})

# def wedding_even(request):
#     objs=story.objects.all
#     return render(request,"index.html",{'result':objs})

# def addition(request):
#     numb1=int(request.POST['num1'])
#     numb2=int(request.POST['num2'])
#     numb3=numb1+numb2
#     return render(request,'result.html',{"val":numb3})