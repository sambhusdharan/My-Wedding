
from django.urls import path
from . import views
urlpatterns=[
    path('',views.new_wedding,name='home'),
     path('memories',views.memories,name='memories'),
    path('image_view/<int:id>',views.imageview,name='image_view')
]
