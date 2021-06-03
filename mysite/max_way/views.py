from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from . import services
from dashboard.forms import *
import json
from datetime import datetime


def home(request):
    if request.GET:
        product = services.get_product_by_id(request.GET.get("product_id", 0))
        return JsonResponse(product)

    categories = services.get_categories()
    products = services.get_products()

    orders = []
    orders_list = request.COOKIES.get("orders")
    if orders_list:
        for key, val in json.loads(orders_list).items():
            orders.append(
                {
                    "product": Product.objects.get(pk=int(key)),
                    "count": val
                }
            )
    ctx = {
        "products": products,
        "categories": categories,
        "orders": orders
    }
    response = render(request, 'max_way/index.html', ctx)
    response.set_cookie("hello", "hello")
    return response


def order_save(request):
    if request.POST and int(request.COOKIES.get("total_price", 0)):
        new_order = Order()
        new_order.all_price = request.COOKIES.get("total_price", 0)
        new_order.products = request.COOKIES.get("orders", {})
        new_order.status = 1
        new_order.created_at = datetime.now()
        new_order.save()
        response = redirect("order", order_id=new_order.pk)
        response.set_cookie("total_price", 0)
        response.set_cookie("orders", dict())

        return response
    else:
        return redirect("home")


def order(request, order_id):
    model = User()
    form = UserForm(request.POST, instance=model)
    order = Order.objects.get(pk=order_id)

    if request.POST:
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    ctx = {
        "order": order
    }
    return render(request, 'max_way/order.html', ctx)
