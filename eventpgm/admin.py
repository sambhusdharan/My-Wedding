from django.contrib import admin
from .models import wedding,story,wedding_event,gallery,wishes
# Register your models here.

admin.site.register(story)
admin.site.register(wedding_event)
admin.site.register(gallery)
admin.site.register(wishes)

class adminwedding(admin.ModelAdmin):
    list_display = ('id','name_of_bride','name_of_groom','place_of_bride','place_of_groom','wedding_place','wedding_date')
admin.site.register(wedding,adminwedding)



    # name_of_bride=models.CharField(max_length=100)
    # name_of_groom=models.CharField(max_length=100)
    # address_of_bride=models.CharField(max_length=100)
    # place_of_bride=models.CharField(max_length=100)
    # address_of_groom=models.CharField(max_length=100)
    # place_of_groom=models.CharField(max_length=100)
    # wedding_place_address=models.CharField(max_length=100)
    # wedding_place= models.CharField(max_length=100)
    # Wedding_quote=models.TextField()
    # image_bride=models.ImageField(upload_to='wed_img/%Y/%m/%d')
    # image_groom=models.ImageField(upload_to='wed_img/%Y/%m/%d')
    # wedding_date=models.DateTimeField(auto_now=False)
