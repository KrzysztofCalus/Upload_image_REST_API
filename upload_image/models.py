from django.db import models


# Create your models here.

class ImageModel(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.image.name


class PlansModel(models.Model):
    name = models.CharField(max_length=68, default="new plan")
    thumbnail_200 = models.BooleanField(default=False)
    thumbnail_400 = models.BooleanField(default=False)
    original_image = models.BooleanField(default=False)
    link = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class UserModel(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    plan = models.OneToOneField(PlansModel, on_delete=models.CASCADE)
