from django.db import models

# Create your models here.
class ImageCaption(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=500)
