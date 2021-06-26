from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListCreateAPIView
from upload_image.models import ImageModel
from upload_image.serializers import PremiumSerializer, BasicSerializer, EnterpriseSerializer
from django.contrib.auth.models import Group


class ImageUploadView(ListCreateAPIView):
    queryset = ImageModel.objects.all()

    def get_serializer_class(self):
        """
        Returning data depending on account tiers
        :return:
        """
        if Group.objects.get(name="basic").user_set.filter(id=self.request.user.id).exists():
            return BasicSerializer
        if Group.objects.get(name="premium").user_set.filter(id=self.request.user.id).exists():
            return PremiumSerializer
        else:
            return EnterpriseSerializer

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
