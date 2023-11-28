from django.db.models import QuerySet
from django.shortcuts import render

from main_app.models import Item, Order
from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'index.html')


def blog(request):
    return render(request, 'blog.html')


def shop(request):
    items = Item.objects.all()
    # print(items[1])  # Add this line for debugging
    context = {'items': items}
    # print(context)
    return render(request, 'shop.html', context)


def contact(request):
    return render(request, 'contact.html')


def shop_details(request):
    return render(request, 'shop-details.html')


def shopping_cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(Customer=customer, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0} #for user not loged in
    context = {'items': items, 'order': order}
    return render(request, 'shopping-cart.html', context)


def blog_details(request):
    return render(request, 'blog-details.html')


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(Customer=customer, complete=False)
        items = order.orderitem_set.all()
        # print(order)
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}  # for user not logged in
    context = {'items': items, 'order': order}
    return render(request, 'checkout.html', context)
