
from django.urls import path
from . import views
urlpatterns=[
    path('',views.new_wedding,name='bride'),
     # path('add',views.wedding_even,name='add')
]
