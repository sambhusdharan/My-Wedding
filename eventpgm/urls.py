
from django.urls import path
from . import views
urlpatterns=[
    path('',views.new_wedding,name='home'),
     path('memories',views.memories,name='memories')
]
