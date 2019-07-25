from django import forms
from django.core import validators
from .models import Blog
def check_z(value):
	if value[0].lower()!= 'z':
		raise forms.ValidationError("the name value shoud be z")

class FormName(forms.Form):
	name = forms.CharField(validators=[check_z])
	email = forms.EmailField()
	vmail = forms.EmailField(label="Varify email")
	text = forms.CharField(widget = forms.Textarea)

	def clean(self):
		email= self.cleaned_data.get('email')
		vmail= self.cleaned_data.get('vmail')

		if vmail!=email:
			raise forms.ValidationError("The email should be verified")

class BlogFrom(forms.Form):
	title = forms.CharField(max_length=30)
	slug =forms.SlugField(label="SLUG")
	email = forms.EmailField()
	vmail = forms.EmailField(label= "Verify Email")
	content = forms.CharField(max_length=400)

	


class BlogModelForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields ='__all__'
