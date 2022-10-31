from email.mime import image
from rest_framework import serializers

class Converter(serializers.Serializer):
    """Serializes the Image"""
    image = serializers.FileField()
    