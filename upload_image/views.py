from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListCreateAPIView
from upload_image.models import ImageModel
from upload_image.serializers import ImageSerializer


class ImageUploadView(ListCreateAPIView):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer
