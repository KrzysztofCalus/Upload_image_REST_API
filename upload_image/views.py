# Create your views here.

from .models import ImageModel, PlansModel, UserModel
from .serializers import PremiumSerializer, BasicSerializer, EnterpriseSerializer
from rest_framework import generics


class ImageUploadView(generics.ListCreateAPIView):
    queryset = ImageModel.objects.all()

    def get_serializer_class(self):
        """
        Returning data depending on account tiers
        :return:
        """

        user = UserModel.objects.get(user_id=self.request.user.id)
        user_plan_id = user.plan_id

        thumb_200 = PlansModel.objects.get(thumbnail_200=True)
        thumb_200_plan_id = thumb_200.id
        thumb_400 = PlansModel.objects.get(thumbnail_400=True)
        thumb_400_plan_id = thumb_400.id

        if user_plan_id == thumb_200_plan_id:
            return BasicSerializer
        elif user_plan_id == thumb_400_plan_id:
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
