from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	return HttpResponse("Hello")

	
def help(request):
	helpdict={"help_insert":"Help Page"} 
	return render(request,'apptwo/help.html' ,context=helpdict)

