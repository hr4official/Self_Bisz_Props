from django.db import models
class subscribe(models.Model):
    email = models.CharField(max_length=30)