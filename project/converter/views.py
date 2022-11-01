from email.mime import image
from multiprocessing import context
from urllib import request
from django import views
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import  ImageData
from . import serializers
from rest_framework.response import Response
# Create your views here.

def test(request):
    data = ImageData.objects.all()
    context = {
        'data' : data
    }
    return render(request,"display.html", context)

class ConverterApiView(viewsets.ModelViewSet):
    serializer_class = serializers.Converter
    queryset = ImageData.objects.all()






