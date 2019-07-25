from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
	return render(request,'basicapp/index.html')

def formcall(request):
	my_dict = {'form' : forms.FormName()  }
	if request.method == "POST":
		form = forms.FormName(request.POST)
		if form.is_valid():
			print(form.cleaned_data['name'])
	return render(request,'basicapp/form_page.html',context = my_dict)
