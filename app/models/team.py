from django.db import models

class team(models.Model):
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='media/team/images')