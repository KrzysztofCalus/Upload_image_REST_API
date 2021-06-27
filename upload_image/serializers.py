from django.template.defaultfilters import upper
from rest_framework import serializers
from .models import ImageModel
from PIL import Image
from sorl.thumbnail import get_thumbnail
import imghdr


class EnterpriseSerializer(serializers.ModelSerializer):
    thumbnail_200 = serializers.SerializerMethodField()
    thumbnail_400 = serializers.SerializerMethodField()

    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = ImageModel
        fields = ['image', 'thumbnail_200', 'thumbnail_400']

    def get_thumbnail_400(self, object):
        """
        Create thumbnail size 400 on height. Save image in cache.
        :param object:
        :return:
        """
        format = upper(imghdr.what('media/' + object.image.name))
        new_height = 400
        image = Image.open('media/' + object.image.name)
        width, height = image.size
        new_width = int(new_height * width / height)
        im = get_thumbnail(object, f'{new_width}x{new_height}', crop='center', quality=99, format=format)
        return "http://127.0.0.1:8000" + im.url

    def get_thumbnail_200(self, object):
        """
        Create thumbnail size 200 on height. Save image in cache.
        :param object:
        :return:
        """
        format = upper(imghdr.what('media/' + object.image.name))
        new_height = 200
        image = Image.open('media/' + object.image.name)
        width, height = image.size
        new_width = int(new_height * width / height)
        im = get_thumbnail(object, f'{new_width}x{new_height}', crop='center', quality=99, format=format)
        return "http://127.0.0.1:8000" + im.url


class PremiumSerializer(serializers.ModelSerializer):
    thumbnail_200 = serializers.SerializerMethodField()
    thumbnail_400 = serializers.SerializerMethodField()

    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = ImageModel
        fields = ['image', 'thumbnail_200', 'thumbnail_400']

    def get_thumbnail_400(self, object):
        format = upper(imghdr.what('media/' + object.image.name))
        new_height = 400
        image = Image.open('media/' + object.image.name)
        width, height = image.size
        new_width = int(new_height * width / height)
        im = get_thumbnail(object, f'{new_width}x{new_height}', crop='center', quality=99, format=format)
        return "http://127.0.0.1:8000" + im.url

    def get_thumbnail_200(self, object):
        format = upper(imghdr.what('media/' + object.image.name))
        new_height = 200
        image = Image.open('media/' + object.image.name)
        width, height = image.size
        new_width = int(new_height * width / height)
        im = get_thumbnail(object, f'{new_width}x{new_height}', crop='center', quality=99, format=format)
        return "http://127.0.0.1:8000" + im.url


class BasicSerializer(serializers.ModelSerializer):
    thumbnail_200 = serializers.SerializerMethodField()

    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = ImageModel
        fields = ['image', 'thumbnail_200']

    def get_thumbnail_200(self, object):
        format = upper(imghdr.what('media/' + object.image.name))
        new_height = 200
        image = Image.open('media/' + object.image.name)
        width, height = image.size
        new_width = int(new_height * width / height)
        im = get_thumbnail(object, f'{new_width}x{new_height}', crop='center', quality=99, format=format)
        return "http://127.0.0.1:8000" + im.url
