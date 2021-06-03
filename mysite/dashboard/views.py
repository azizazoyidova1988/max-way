from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from max_way.models import *
from .services import *
from .forms import *
from django.shortcuts import render, redirect


def login_required_decorator(f):
    return login_required(f, login_url="login")


@login_required_decorator
def status(request, pk, status):
    model = Order.objects.get(id=pk)
    model.status = status
    model.save()
    return redirect("order_list")


@login_required_decorator
def dashboard_page(request):
    status = get_status_info([1, 2, 3])
    stat_1 = get_status_1()[0]['count']
    stat_2 = get_status_2()[0]['count']
    stat_3 = get_status_3()[0]['count']
    categories = get_categories_products_count()
    categories_count = get_categories_count()
    products_count = get_products_count()
    users_count = get_users_count()

    statuses = {
        "order": stat_1,
        "done": stat_2,
        "failed": stat_3,
    }

    ctx = {
        "categories": categories,
        "categories_count": categories_count,
        "products_count": products_count,
        "users_count": users_count,
        "statuses": statuses,
        "status": status,

    }
    return render(request, 'dashboard/index.html', ctx)


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


@login_required_decorator
def category_list(request):
    categories = get_categories()
    ctx = {
        "categories": categories
    }
    return render(request, 'dashboard/category/list.html', ctx)


@login_required_decorator
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


@login_required_decorator
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


@login_required_decorator
def category_delete(request, category_id):
    model = Category.objects.get(id=category_id)
    model.delete()
    return redirect("category_list")


@login_required_decorator
def product_list(request):
    products = get_products()
    ctx = {
        "products": products
    }
    return render(request, 'dashboard/product/list.html', ctx)


@login_required_decorator
def product_create(request):
    model = Product()
    form = ProductForm(request.POST, request.FILES, instance=model)
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


@login_required_decorator
def product_edit(request, product_id):
    model = Product.objects.get(id=product_id)
    form = ProductForm(request.POST or None, request.FILES, instance=model)
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


@login_required_decorator
def product_delete(request, product_id):
    model = Product.objects.get(id=product_id)
    model.delete()
    return redirect('product_list')


def user_list(request):
    users = get_user()
    ctx = {
        "users": users
    }
    return render(request, 'dashboard/user/list.html', ctx)


@login_required_decorator
def order_list(request):
    status = get_status_info([1, 2, 3])
    filter = "all"
    if request.POST:
        filter = request.POST.get("order_filter")

        if filter == "done":
            status = get_status_info([2])

        if filter == "failed":
            status = get_status_info([3])

    ctx = {
        "status": status,
        "filter": filter,
    }
    return render(request, 'dashboard/order/list.html', ctx)


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
