from pyexpat import model
from django.db import models

# Create your models here.

    
class ImageData(models.Model):
    image = models.FileField(upload_to='pics')

    def __str__(self):
        return self.image