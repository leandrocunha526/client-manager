from django.forms import ModelForm
from django import forms
from .models import Product, Category


class ProductForm(ModelForm):
    price = forms.DecimalField(max_digits=8, decimal_places=2, widget=forms.NumberInput(attrs={'placeholder': 'Preço do produto'}))
    class Meta:
        model = Product
        widgets = {
			'name': forms.TextInput(attrs={'placeholder': 'Nome o produto'}),
			'description': forms.TextInput(attrs={'placeholder': 'Descrição do produto'}),
			'quantity': forms.NumberInput(attrs={'placeholder': 'Quantidade de produto'})
        }
        fields = ['name', 'price', 'category', 'supplier', 'description', 'quantity']
        labels = {
            'name': ("Nome"),
            'description': ("Descrição"),
            'price': ("Preço"),
            'category': ("Categoria"),
            'supplier': ("Fornecedor"),
            'quantity': ("Quantidade")
        }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome da categoria'})
        }
        fields = ['name']
        labels = {
            'name': ("Nome"),
        }
