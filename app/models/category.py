from django.db import models

class category(models.Model):
    category = models.CharField(max_length=20)
    sub_category = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='media/category/images')