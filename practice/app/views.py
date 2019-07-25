from django.shortcuts import render
from django.http import HttpResponse
from app.models import Hello
from app.forms import Enter
# Create your views here.

def hello(request):
	lis = Hello.objects.all()
	output = ', '.join([q.questions for q in lis])
	return HttpResponse(output)

def html(request):
	k = Enter()
	return render(request,'app/test.html', {'here':k})

def css(request):
	return HttpResponse("So CSS is working too")

	
