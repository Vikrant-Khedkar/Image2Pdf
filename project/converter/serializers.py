from email.mime import image
from rest_framework import serializers
from .models import ImageData

class Converter(serializers.ModelSerializer):
    """Serializes the Image"""
    class Meta:
        model = ImageData
        fields = ('image',)
    