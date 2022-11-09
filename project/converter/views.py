from email.mime import image
from multiprocessing import context
from urllib import request
from django import forms, views
from PIL import Image
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from django import forms
from .models import ImageData
from . import serializers
from rest_framework.response import Response
import img2pdf
# Create your views here.


def uploadimage(request):
    """Upload given image to the database"""
    return render(request, 'index.html')

def diplaypdf(request):
    return HttpResponseRedirect("C:\Developer\Django practice\ImageToPdf\project\media\converted.pdf")


def test(request):
    """Display latest uploaded image to the user"""
    data = ImageData.objects.latest('id')
    base = 'C:\Developer\Django practice\ImageToPdf\project'
    url = data.image.url
    link = base+url
    image_1 = Image.open(link)
    im_1 = image_1.convert('RGB')
    pdf = im_1.save(r'C:\Developer\Django practice\ImageToPdf\project\media\converted.pdf')
    context = {
        'data': data,
        'pdf':pdf
    }

    return render(request, "display.html", context)


class ConverterApiView(viewsets.ModelViewSet):
    serializer_class = serializers.Converter
    queryset = ImageData.objects.all()

    

