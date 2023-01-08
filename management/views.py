from django.shortcuts import render,redirect
from eventpgm.models import *
from .models import contact

# Create your views here.
def services(request):
    obj = wedding.objects.all()
    return render(request,'services.html',{'results':obj})

def photogallery(request):
    obj = wedding.objects.all()
    image = gallery.objects.all()
    return render(request, 'gallery.html',{'results':obj,'gallery':image})

def contacts(request):
    obj = wedding.objects.all()
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data=contact.objects.create(firstname=first_name,lastname=last_name,email=email,subject=subject,message=message)
        data.save()
        return redirect('contact')
    return render(request,'contact.html',{'results':obj})
