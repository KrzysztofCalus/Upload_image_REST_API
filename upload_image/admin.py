from django.contrib import admin
from .models import ImageModel, PlansModel, UserModel


# Register your models here.

@admin.register(ImageModel)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'owner')


@admin.register(PlansModel)
class PlansAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumbnail_200', 'thumbnail_400', 'original_image', 'link')


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan')
