from django import forms
from project_app.models import User

class NewUser(forms.ModelForm):
	class Meta:
		model = User 
		fields = '__all__'