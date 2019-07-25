from django.shortcuts import render
from .forms import UserInfo,UserProfileInfoForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
# Create your views here.

def index(request):
	return render(request,'basic_app/index.html')

def register(request):
	registered = False
	if request.method=='POST':
			user_form = UserInfo(request.POST)
			profile_form = UserProfileInfoForm(request.POST)

			if user_form.is_valid() and profile_form.is_valid():
				user = user_form.save()
				name= user.username
				user.set_password(user.password)
				user.save()
				profile = profile_form.save(commit=False)
				profile.user = user
				if 'profile_pick' in request.FILES:
					profile.profile_pick = request.FILES['profile_pick']
				profile.save()
				registered = True
				
	else:
		user_form= UserInfo()
		profile_form= UserProfileInfoForm()


	return render(request,'basic_app/register.html',{'registered':registered,'user_form':user_form,'profile_form':profile_form})


@login_required
def user_logout(request):
	logout(request)
	return index(request)

def user_login(request):
	if request.method =='POST':
		username = request.POST.get('username')
		password= request.POST.get('password')

		user = authenticate(username= username, password=password)

		if user:
			if user.is_active:
				login(request,user)
				return index(request)
			else:
				return HttpResponse("Account not Active")
		else:
			print("Login is failed")
			return HttpResponse("Invalid login detail supplied")
	else:
		return render(request,'basic_app/login.html',{})


