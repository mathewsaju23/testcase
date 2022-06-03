from django.urls import path
from .views import ProductViews, CustomerViews, CollectionViews,  ProductDetail, CustomerDetail, UserCartQuantity, UserCartView, UserCartViews

urlpatterns = [
    path('products/', ProductViews.as_view()),
    path('products/<int:pk>', ProductDetail.as_view()),

    path('customers/', CustomerViews.as_view()),
    path('customers/<int:pk>', CustomerDetail.as_view()),

    path('collections/', CollectionViews.as_view()),


    path('usercart/', UserCartView.as_view()),
    path('usercart/<int:pk>', UserCartViews.as_view()),
    path('usercartqn/<int:pk>', UserCartQuantity.as_view()),










]
