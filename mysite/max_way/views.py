from django.shortcuts import render
from . import services


def home(request):
    categories = services.get_categories()
    products = services.get_products()
    ctx = {
        "categories": categories,
        "products": products
    }
    return render(request, 'index.html', ctx)


def order(request):
    return render(request, 'order.html')
