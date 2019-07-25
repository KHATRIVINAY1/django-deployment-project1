from django.contrib import admin
from django.urls import path,include
from . import views
app_name = 'basic_app'
urlpatterns = [path('',views.index,name='home'),
				path('register/',views.register,name= 'register'),
				path('user_login',views.user_login,name='user_login')
	
]
