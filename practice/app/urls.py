from . import views
from django.urls import path
from django.conf.urls import  url
urlpatterns = [path('',views.hello, name= "Hello"),
				path('say/',views.html, name='Html'),
				url(r'^kh/',views.css, name='css')
				]