from django.db import models

# Create your models here.


class Lead(models.Model):
    name = models.CharField(max_length=128)
    email= models.EmailField(unique= True)
    message = models.CharField(max_length=512, blank= True)
    created = models.DateTimeField(auto_now_add=True)
    
