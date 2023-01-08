from django.urls import path
from . import views
urlpatterns=[
    path('',views.services,name='services'),
    path('gallery/',views.photogallery,name='photogallery'),
    path('contact/',views.contacts,name='contact')
]
