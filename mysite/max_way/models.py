from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    combo=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    description = models.CharField(max_length=250, blank=False, null=False)
    image = models.ImageField(upload_to="images/", blank=False, null=False)
    price = models.IntegerField( blank=False, null=False,default=0)
    amount = models.IntegerField( blank=False, null=False,default=0)
    category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)



class Order(models.Model):
    product=models.JSONField()
    all_price = models.IntegerField( blank=False, null=False,default=0)
    amount = models.IntegerField( blank=False, null=False,default=0)
    status=models.IntegerField( blank=False, null=False,default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    first_name=models.TextField(max_length=100,blank=False,null=False)
    last_name=models.TextField(max_length=100,blank=False,null=False)
    phone_number=models.CharField(max_length=20,blank=False,null=False)
    price_type=models.IntegerField(blank=False,null=False,default=0)
    address=models.TextField(max_length=100,blank=False,null=False)
    order = models.ForeignKey(Order, blank=False, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
