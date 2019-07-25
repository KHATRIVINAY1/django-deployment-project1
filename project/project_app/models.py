from django.db import models

# Create your models here.

class User(models.Model):
	first_name = models.CharField(max_length = 120, unique =True)
	last_name  = models.CharField(max_length=110,unique=True)
	email= models.EmailField(max_length=120, unique= True)
