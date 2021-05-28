from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_page, name="dashboard"),
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),

    path('category_list/', views.category_list, name='category_list'),
    path('category/add/', views.category_create, name="category_add"),
    path('category/<int:category_id>/edit/', views.category_edit, name="category_edit"),
    path('category/<int:category_id>/delete/', views.category_delete, name="category_delete"),

    path('product_list/', views.product_list, name='product_list'),
    path('product/add/', views.product_create, name="product_add"),
    path('product/<int:product_id>/edit/', views.product_edit, name="product_edit"),
    path('product/<int:product_id>/delete/', views.product_delete, name="product_delete"),

    path('order_list/', views.order_list, name='order_list'),
    path('order/add/', views.order_create, name="order_add"),
    path('order/<int:order_id>/edit/', views.order_edit, name="order_edit"),
    path('order/<int:order_id>/delete/', views.order_delete, name="order_delete"),

    path('user_list/', views.user_list, name='user_list'),
    path('user/add/', views.user_create, name="user_add"),
    path('user/<int:user_id>/edit/', views.category_edit, name="user_edit"),
    path('user/<int:user_id>/delete/', views.category_delete, name="user_delete")

]
