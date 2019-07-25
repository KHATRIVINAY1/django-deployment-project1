from django import forms

class Enter(forms.Form):
	name = forms.CharField(max_length =200)
	email = forms.EmailField(max_length= 200)
	phone = forms.IntegerField()