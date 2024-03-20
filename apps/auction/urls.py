from django.urls import path
from .views import search_auctions, auction_detail, create_auction

urlpatterns = [
    path('', search_auctions, name='auction'),
    path('create_auction/', create_auction, name='create_auction'),
    path('auction/<int:auction_id>/', auction_detail, name='auction_detail')
]
