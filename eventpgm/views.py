from django.shortcuts import render
#from django.http import HttpResponse
from .models import *

# Create your views here.
def new_wedding(request):
    obj=wedding.objects.all()
    event=wedding_event.objects.all()
    stories=story.objects.all()
    photos=gallery.objects.all()
    return render(request,"index.html",{'results':obj,'event':event ,'story':stories,'gallery':photos})

def memories(request):
    detail=wedding.objects.all()
    memory=story.objects.all()
    return render(request,"story.html",{'detail':detail,'memory':memory})

def addition(request):
    result = wedding.objects.all()
    return render(request,'check.html',{"val":result})

