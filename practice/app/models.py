from django.db import models
# Create your models here.

class Hello(models.Model):
	questions= models.CharField(max_length=200)
	date = models.DateTimeField('date published')
	def __str__(self):
		return (self.questions,self.date)

class Choice(models.Model):
	questions = models.ForeignKey(Hello,on_delete= models.CASCADE)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField(default = 0 )
