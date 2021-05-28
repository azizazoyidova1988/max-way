from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from max_way.models import *
from max_way.services import *
from .forms import *
from django.shortcuts import render, redirect


def login_required_decorator(f):
    return login_required(f, login_url="login")


@login_required_decorator
def dashboard_page(request):
    # categories = servises.get_categories_news_count()
    # categories_count=servises.get_categories_count()
    # authors_count=servises.get_categories_count()
    # news_count=servises.get_news_count()
    # references_count=servises.get_references_count()
    # views=servises.get_views()
    # print(views)
    # ctx = {
    #     "categories": categories,
    #     "categories_count":categories_count,
    #     "authors_count":authors_count,
    #     "news_count":news_count,
    #     "references_count":references_count,
    #     "views": views
    # }
    return render(request, 'dashboard/index.html')


def dashboard_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'dashboard/login.html')


def dashboard_logout(request):
    logout(request)
    return redirect('login')


def category_list(request):
    categories = get_categories()
    ctx = {
        "categories": categories
    }
    return render(request, 'dashboard/category/list.html', ctx)


def category_create(request):
    model = Category()
    form = CategoryForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/category/form.html', ctx)


def category_edit(request, category_id):
    model = Category.objects.get(id=category_id)
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/category/form.html', ctx)


def category_delete(request, category_id):
    model = Category.objects.get(id=category_id)
    model.delete()
    return redirect("category_list")


def product_list(request):
    products = get_products()
    ctx = {
        "products": products
    }
    return render(request, 'dashboard/product/list.html', ctx)


def product_create(request):
    model = Product()
    form = ProductForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            model.save()
            return redirect('product_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/product/form.html', ctx)


def product_edit(request, product_id):
    model = Product.objects.get(id=product_id)
    form = ProductForm(request.POST or None, request.files, instance=model)
    if request.POST:
        if form.is_valid():
            model.save()
            return redirect('product_list')
        else:
            print(form.error)
    ctx = {
        'form': form

    }
    return render(request, 'dashboard/product/form.html', ctx)


def product_delete(request, product_id):
    model = Product.objects.get(id=product_id)
    model.delete()
    return redirect('product_list')


def order_list(request):
    orders = get_order()
    ctx = {
        "orders": orders
    }
    return render(request, 'dashboard/order/list.html',ctx)


def order_create(request):
    model = Order()
    form = OrderForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            model.save()
            return redirect('order_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/order/form.html', ctx)


def order_edit(request, order_id):
    model = Order.objects.get(id=order_id)
    form = OrderForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            model.save()
            return redirect('order_list')
        else:
            print(form.error)
    ctx = {
        'form': form

    }
    return render(request, 'dashboard/order/form.html', ctx)


def order_delete(request, order_id):
    model = Order.objects.get(id=order_id)
    model.delete()
    return redirect('order_list')


def user_list(request):
    users = get_order()
    ctx = {
        "users": users
    }
    return render(request, 'dashboard/user/list.html', ctx)


def user_create(request):
    model = User()
    form = UserForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            model.save()
            return redirect('user_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/user/form.html', ctx)


def user_edit(request, user_id):
    model = User.objects.get(id=user_id)
    form = UserForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            model.save()
            return redirect('user_list')
        else:
            print(form.error)
    ctx = {
        'form': form

    }
    return render(request, 'dashboard/user/form.html', ctx)


def user_delete(request, user_id):
    model = User.objects.get(id=user_id)
    model.delete()
    return redirect('user_list')
