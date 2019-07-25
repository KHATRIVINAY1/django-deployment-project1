from django.conf.urls import url
from sec_app import views
urlpatterns=[
url(r'^$',views.help,name='help')
] 