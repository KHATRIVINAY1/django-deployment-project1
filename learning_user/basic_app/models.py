from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
	user = models.ForeignKey(User,models.SET_NULL,null=True,blank=True)
	portfolio_site  = models.URLField(blank= True)
	profile_pick = models.ImageField(upload_to='profile_pic',blank=True)


	def __str__(self):
		try:
			return self.user.username
		except:
			return "Admin"