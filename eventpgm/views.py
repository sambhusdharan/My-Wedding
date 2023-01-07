from django.shortcuts import render
from django.db.models import Count
#from django.http import HttpResponse
from .models import *

# Create your views here.
def new_wedding(request):
    obj=wedding.objects.all()
    event=wedding_event.objects.all()
    stories=story.objects.all()
    photos=gallery.objects.all()
    wishing=wishes.objects.all()
    print(wishing)
    return render(request,"index.html",{'results':obj,'event':event ,'story':stories,'gallery':photos,'wish':wishing})

def memories(request):
    detail=wedding.objects.all()
    stories = story.objects.all()
    return render(request,"story.html",{'detail':detail,'story':stories})

def addition(request):
    result = wedding.objects.all()
    return render(request,'check.html',{"val":result})

def imageview(request,id,count=0):
    image=gallery.objects.all().filter(id=id)
    for i in image:
        count=count+1
        print(count)
    return render(request,'image_viewer.html',{'image':image})