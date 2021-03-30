from django.db import models
class contact(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    message = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
