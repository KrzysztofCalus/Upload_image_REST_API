from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ImageModel(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.image.name
