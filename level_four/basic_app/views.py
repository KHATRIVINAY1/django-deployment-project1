from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'basic_app/index.html')

def others(request):
	return render(request, 'basic_app/others.html')

def relative(request):
	return render(request,'basic_app/relative.html')