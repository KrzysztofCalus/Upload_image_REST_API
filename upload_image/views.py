from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListCreateAPIView
from upload_image.models import ImageModel
from upload_image.serializers import ImageSerializer


class ImageUploadView(ListCreateAPIView):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer

    def perform_create(self, serializer):
        """
        Saving image for logged user
        :param serializer:
        """
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        Getting images for logged user
        :return:
        """
        user = self.request.user
        return ImageModel.objects.filter(owner_id=user)
