from django.shortcuts import render
from project_app.forms import NewUser
# Create your views here.

def index(request):
	return render(request,'project_app/index.html')

def users(request):
	form = NewUser()

	if request.method =='POST':
		form = NewUser(request.POST)
		
		if form.is_valid():
			form.save(commit= True)
			return index(request)
		else:
			print("form is invalid please send a valid form")

	return render(request,'project_app/users.html',context = {"form":form})
	