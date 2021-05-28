from django.shortcuts import render
from django.http import JsonResponse
from . import services
import json


def home(request):
    if request.GET:
        product = services.get_product_by_id(request.GET.get("product_id", 0))
        for prod in product:
            return JsonResponse(prod)

    categories = services.get_categories()
    products = services.get_products()

    ctx = {
        "categories": categories,
        "products": products
    }
    return render(request, 'max_way/index.html', ctx)


def order(request):
    return render(request, 'max_way/order.html')
