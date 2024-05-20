from rest_framework import generics
from ..auction.models import Hotwheel
from .serializers import HotwheelSerializer


class HotwheelsListView(generics.ListAPIView):
    queryset = Hotwheel.objects.all()
    serializer_class = HotwheelSerializer
