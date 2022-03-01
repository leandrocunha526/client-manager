from django.forms import ModelForm
from .models import Product, Category


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'description']
        labels = {
            'name': ("Nome"),
            'description': ("Descrição"),
            'price': ("Preço"),
            'category': ("Categoria")
        }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': ("Nome"),
        }
