from django.db import models

# Create your models here.

class Topic(models.Model):
	top_name = models.CharField(max_length = 254, unique =True )

	def __str__ (self):
		return self.top_name

class Webpage(models.Model):
	topic = models.ForeignKey(Topic,models.PROTECT)
	name = models.CharField(max_length = 259, unique=True)
	url = models.URLField (unique =True)

	def __str__(self):
		return self.name

class AccessRecord(models.Model):
	name = models.ForeignKey(Webpage,models.PROTECT)
	date = models.DateField()

	def __str__ (self):
		return str(self.date)