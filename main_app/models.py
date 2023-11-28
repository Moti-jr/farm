from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name


class Item(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True, default='static/app/img/product-1.jpg')
    digital = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url


class Order(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    # item = models.ForeignKey(Item, on_delete=models.CASCADE)
    # quantity = models.IntegerField(default=1)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.item.price * self.quantity
        return total


class ShippingAddress(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    Order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=30, null=True)
    zipcode = models.CharField(max_length=30, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


