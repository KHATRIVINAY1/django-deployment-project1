from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
	return render(request, 'hope_app/index.html')

def help(request):
	dict_ = {'help': "here we help you"}
	return render(request,'hope_app/help.html', context =dict_)