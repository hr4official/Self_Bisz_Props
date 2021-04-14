from django.db import models
from app.models.category import Category
class subcat(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    sub_category = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='media/category/images')