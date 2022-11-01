import imp
from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'converter',views.ConverterApiView,basename='converter')

urlpatterns = [
     path('test/',views.test,name='test'),
     path('',include(router.urls)),
     path('upload/',views.uploadimage,name='upload'),
]