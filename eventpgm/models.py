from django.db import models

# Create your models here.

class wedding(models.Model):
    name_of_bride=models.CharField(max_length=100)
    name_of_groom=models.CharField(max_length=100)
    address_of_bride=models.CharField(max_length=100)
    place_of_bride=models.CharField(max_length=100)
    address_of_groom=models.CharField(max_length=100)
    place_of_groom=models.CharField(max_length=100)
    wedding_place_address=models.CharField(max_length=100)
    wedding_place= models.CharField(max_length=100)
    Wedding_quote=models.TextField()
    image_bride=models.ImageField(upload_to='wed_img/%Y/%m/%d')
    image_groom=models.ImageField(upload_to='wed_img/%Y/%m/%d')
    wedding_date=models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.name_of_groom


class wedding_event(models.Model):
    ceremony_from_time = models.TimeField(auto_now=False)
    ceremony_to_time = models.TimeField(auto_now=False)
    date_ceremony=models.DateField(auto_now=False)
    desc_ceremony = models.TextField()
    party_from_time = models.TimeField(auto_now=False)
    party_to_time = models.TimeField(auto_now=False)
    date_party = models.DateField(auto_now=False)
    desc_party = models.TextField()
    def __str__(self):
        return self.date_ceremony

class story(models.Model):
    First_meet_date=models.DateField(auto_now=False)
    Describe_first_meet=models.TextField()
    Image_of_first_meet=models.ImageField(upload_to='wed_img/%Y/%m/%d')
    First_date = models.DateField(auto_now=False)
    Describe_first_date = models.TextField()
    Image_of_first_date = models.ImageField(upload_to='wed_img/%Y/%m/%d')
    Relationship_date = models.DateField(auto_now=False)
    Say_something_about_Relationship= models.TextField()
    Image_after_in_a_Relationship = models.ImageField(upload_to='wed_img/%Y/%m/%d')
    def __str__(self):
       return self.First_meet_date

class gallery(models.Model):
    Gallery_name = models.CharField(max_length=100)
    photo_1 = models.ImageField(upload_to='wed_img/%Y/%m/%d/' )
    photo_2 = models.ImageField(upload_to='wed_img/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='wed_img/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='wed_img/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='wed_img/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='wed_img/%Y/%m/%d/', blank=True)
    photo_7 = models.ImageField(upload_to='wed_img/%Y/%m/%d/', blank=True)
    photo_8 = models.ImageField(upload_to='wed_img/%Y/%m/%d/', blank=True)
    photo_9 = models.ImageField(upload_to='wed_img/%Y/%m/%d/', blank=True)
    photo_10 = models.ImageField(upload_to='wed_img/%Y/%m/%d/', blank=True)
    photo_11 = models.ImageField(upload_to='wed_img/%Y/%m/%d/', blank=True)
    photo_12 = models.ImageField(upload_to='wed_img/%Y/%m/%d/', blank=True)
    def __str__(self):
       return self.Gallery_name

class wishes(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='friends',blank=True)
    Wishes = models.TextField()
    def __str__(self):
       return self.name