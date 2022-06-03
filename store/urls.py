from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    # Leave as empty string for base url
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),




]
