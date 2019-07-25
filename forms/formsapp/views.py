from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import FormName,BlogFrom,BlogModelForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from .models import Blog

# Create your views here.

def index(request):
	return render(request,'formsapp/index.html')

def form_name_view(request):
	form = FormName(request.POST)
	
	if form.is_valid():
		return index(request)
	my_dict= {'form':form}

	return render(request,'formsapp/form_page.html', my_dict)

#@login_required(login_url='/login/karo') 	#we can also set this login_url at setting .py file by LOGIN_URL = '\login krlo phle'
@staff_member_required
def create(request):
	form = BlogFrom(request.POST)
	if form.is_valid():
		print(request.user)
		obj = Blog()
		obj.title = form.cleaned_data.get('title')
		obj.slug = form.cleaned_data.get('slug')
		obj.email = form.cleaned_data.get('email')
		obj.content = form.cleaned_data.get('content')
		obj.save()

		form=BlogFrom()

	return render(request,'formsapp/create.html',{'form':form})

def createmodel(request):
	form = BlogModelForm(request.POST)
	if form.is_valid():
		form.save()

		form = BlogModelForm()

	return render(request,'formsapp/modelforms.html',{'form':form})