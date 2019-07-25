from django.db import models
# Create your models here.
class Questions(models.Model):
	que = models.CharField(max_length=40)
	ans = models.IntegerField()