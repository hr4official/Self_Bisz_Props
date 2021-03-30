from django.db import models

class portfulio(models.Model):
    name = models.CharField(max_length=20)
    sub_name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='media/portfulio/images')