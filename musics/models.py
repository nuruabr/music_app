from django.db import models
from django.db.models import Model

# Create your models here.

class MusicsApp_Models(models.Model):
    music_name =models.CharField(max_length=150)
    music_logo = models.ImageField(blank=True, upload_to='blog_images')
    # music_file =models.FileField()
    music_writer=models.CharField(max_length=500)
    music_singer=models.CharField(max_length=400)
    
    def __str__(self):
        return self.music_name