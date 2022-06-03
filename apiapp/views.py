

from rest_framework import views
from rest_framework.response import Response
from .serializers import ProductSerializer, CustomerSerializer, CollectionSerializer,  UserCartCreateSerializer, UserCartSerializer
from .models import Customer, Product, Collection,  UserCart

from rest_framework import generics


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductViews(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerViews(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CollectionViews(generics.ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class UserCartView(generics.ListCreateAPIView):
    queryset = UserCart.objects.all()
    serializer_class = UserCartCreateSerializer


class UserCartViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserCart.objects.all()
    serializer_class = UserCartSerializer


class UserCartQuantity(views.APIView):
    def get(self, *args, **kwargs):
        pk = kwargs["pk"]
        cart = UserCart.objects.get(pk=pk)
        cart_data = UserCartSerializer(cart)
        total_price = 0
        for pdt in cart_data.data["products"]:
            total_price += pdt["product_price"]
        return Response(data={'data': cart_data.data, "total_price": total_price})
