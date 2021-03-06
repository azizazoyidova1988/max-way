from django import forms
from max_way.models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category()
        fields = "__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product()
        fields = "__all__"



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order()
        fields = "__all__"



class UserForm(forms.ModelForm):
    class Meta:
        model = User()
        fields = "__all__"
