
from rest_framework import serializers
from .models import Product, Customer, Collection, UserCart


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['cust_id', 'phone', 'email']


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['pk', 'title']

        # products_count = serializers.IntegerField(read_only=True)

        # def get_products_count(self, Product):
        #     return Count('products')


class UserCartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCart
        fields = ["user", "products"]


class UserCartSerializer(serializers.ModelSerializer):  # cartitem
    products = ProductSerializer(many=True)

    class Meta:
        model = UserCart
        fields = ["products"]
