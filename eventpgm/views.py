from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render,redirect
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

def base(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
    admin_detail = User.objects.get(is_superuser=True)
    admin_email = admin_detail.email
    send_mail(
        'You have one message !',
        'one is attenting the wedding with name: ' + name + ' and email id: ' + email + ' Please note this message',
        'myweddingcorp23@gmail.com',  # from email address
        [admin_email],  # To email address
        fail_silently=False,
          )
    return redirect('home')
