from django.db import models

# Create your models here.
class contact(models.Model):
    firstname=models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.TextField()
    message=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.firstname