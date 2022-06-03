from django.conf import settings
from django.db import models


from django.core.validators import MinValueValidator
# Create your models here.


class Collection(models.Model):
    title = models.CharField(max_length=255, primary_key=True)
    featured_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True, related_name='+', blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


class Product(models.Model):

    product_name = models.CharField(max_length=200)
    description = models.TextField()
    product_price = models.FloatField()
    inventory = models.PositiveIntegerField()
    collection = models.ForeignKey(
        Collection, on_delete=models.CASCADE, related_name='products', null=True)

    def __str__(self) -> str:
        return self.product_name


class Customer(models.Model):
    cust_id = models.CharField(max_length=50, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.first_name


class UserCart(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(
        Product, symmetrical=False)

    def __str__(self) -> str:
        return self.user.first_name
