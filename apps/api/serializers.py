from rest_framework import serializers
from ..auction.models import Hotwheel


class HotwheelSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Hotwheel
        fields = '__all__'
