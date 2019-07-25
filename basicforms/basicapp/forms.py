from django import forms
from django.core import validators

def check_for_z(value):
	if value[0].lower() != 'z':
		raise forms.ValidationError("Gotch Ya")

class FormName(forms.Form):
	name = forms.CharField(validators = [check_for_z])
	email = forms.EmailField()
	v_email = forms.EmailField(label ="Enter your mail again")
	text = forms.CharField(widget = forms.Textarea)
	botcatcher = forms.CharField(required = False , 
								widget =forms.HiddenInput,
								validators = [validators.MaxLengthValidator(0)])

	'''def clean_botcather(self):
		botcatcher = self.clean_data['botcatcher']
		if len(botcatcher)> 0:
			raise forms.ValidationError("Gotch you bot")
		return botcatcher'''

	def clean(self):
		clean_all_data = super().clean()
		email = clean_all_data['email']
		vmail =clean_all_data['v_email']

		if email != vmail:
			raise forms.ValidationError("Make sure it work")