from django.contrib import admin

from main_app.models import Customer, Item, OrderItem, ShippingAddress, Order

# Register your models here.
admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

