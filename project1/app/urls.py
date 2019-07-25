from django.urls import path
from app import views

urlpatterns =[path('<int:pos>/',views.index,name='index'),
path('base/',views.base,name='base')
]