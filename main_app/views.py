from django.db.models import QuerySet
from django.shortcuts import render

from main_app.models import Item


# Create your views here.


def home(request):
    return render(request, 'index.html')


def blog(request):
    return render(request, 'blog.html')


def shop(request):
    items = Item.objects.all()
    # print(items)  # Add this line for debugging
    context = {'items': items}
    # print(context)
    return render(request, 'shop.html', context)


def contact(request):
    return render(request, 'contact.html')


def shop_details(request):
    return render(request, 'shop-details.html')


def shopping_cart(request):
    return render(request, 'shopping-cart.html')


def blog_details(request):
    return render(request, 'blog-details.html')


def checkout(request):
    return render(request, 'checkout.html')
