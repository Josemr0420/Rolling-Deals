# your_app_name/serializers.py

from rest_framework import serializers
from ..auction.models import Hotwheel, Auction

class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = ['start_time', 'end_time', 'status', 'starting_bid', 'user']

class HotwheelSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    auction = AuctionSerializer(read_only=True, source='auction_set', many=True)

    class Meta:
        model = Hotwheel
        fields = '__all__'

