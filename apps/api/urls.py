from django.urls import path
from .views import HotwheelsListView

urlpatterns = [
    path('hotwheels/', HotwheelsListView.as_view(), name='hotwheels-list'),
]
