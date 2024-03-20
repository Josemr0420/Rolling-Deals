from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.auction.views import create_auction
from apps.user_management import views

urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("register/", views.RegisterPage.as_view(), name="register"),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path("", views.home, name="home")
]

