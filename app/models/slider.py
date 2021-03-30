from django.db import models
class slider(models.Model):
    photo = models.ImageField(upload_to='media/slider/images')