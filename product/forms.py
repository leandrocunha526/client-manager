from django.forms import ModelForm
from .models import Product, Category


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
