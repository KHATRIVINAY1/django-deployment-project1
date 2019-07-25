from django.shortcuts import render
from app.models import Questions
# Create your views here.

def index(request,pos):
	question  = Questions.objects.get(id=pos)
	dic = {'question':question.que,
	'answer':question.ans}
	return render(request,'app/index.html',context=dic)

def base(request):
	return render(request,'app/base.html')