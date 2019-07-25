from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'basic_app'
urlpatterns =[path('', views.index, name="index"),
			path('relative/',views.relative,name='relative'),
			path('others/',views.others, name = 'others'),]
