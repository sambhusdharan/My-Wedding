from django.shortcuts import render
from eventpgm.models import *
# Create your views here.
def services(request):
    obj = wedding.objects.all()
    return render(request,'services.html',{'results':obj})

def photogallery(request):
    obj = wedding.objects.all()
    image = gallery.objects.all()
    return render(request, 'gallery.html',{'results':obj,'gallery':image})

def contact(request):
    obj = wedding.objects.all()
    return render(request,'contact.html',{'results':obj})
