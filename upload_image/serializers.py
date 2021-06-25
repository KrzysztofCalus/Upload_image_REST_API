from rest_framework import serializers
from upload_image.models import ImageModel


class ImageSerializer(serializers.ModelSerializer):
    small_image = serializers.SerializerMethodField()

    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = ImageModel
        fields = ['image', 'small_image']

    def get_small_image(self, object):
        """
        Give additional field in JSON
        :param object:
        :return:
        """
        return "http://127.0.0.1:8000" + object.image.url
