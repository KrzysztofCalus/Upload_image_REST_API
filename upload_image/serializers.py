from rest_framework import serializers
from upload_image.models import ImageModel


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = ImageModel
        fields = ['image']
