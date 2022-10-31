from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
     path('',views.test,name='test'),
     path('api/',views.ConverterApiView.as_view()),
]