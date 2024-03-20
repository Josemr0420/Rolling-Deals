from django.urls import path
from . import views

urlpatterns = [
    path('pay/', views.pay, name = 'pay'),
    path('end_transaction/', views.end_transaction, name='end_transaction'),
]
