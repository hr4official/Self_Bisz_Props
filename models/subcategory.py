from django.db import models

class subcategory(models.Model):
    Business_name = models.CharField(max_length=30)
    City_name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='media/subcategory/images')