from django.forms import ModelForm
from sales.models import Item, Sale


class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['tax', 'discount', 'client', 'datetime', 'status']
        labels = {
            'tax': ("Imposto"),
            'discount': ("Outros descontos (como taxas de envio)"),
            "datetime": ("Data e hora"),
            "client": ("Cliente"),
            'status': ("Estado (status da compra)"),
        }


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['products', 'quantity', 'discount', 'sales']
        labels = {
            'products': ("Produto"),
            'quantity': ("Quantidade"),
            'discount': ("Descontos para ofertar"),
            'sales': ('Selecione a venda')
        }
