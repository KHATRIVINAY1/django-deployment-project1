from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=30)
	slug =models.SlugField()
	email = models.EmailField()
	content = models.TextField()