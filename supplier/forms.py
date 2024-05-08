from django import forms
from .models import Supplier


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome da empresa'}),
            'postal_code': forms.TextInput(
                attrs={'placeholder': '00000-000'}),
            'street_address': forms.TextInput(attrs={'placeholder': 'Nome da rua'}),
            'number': forms.TextInput(attrs={'placeholder': 'Número'}),
            'city': forms.TextInput(attrs={'placeholder': 'Cidade'}),
            'state': forms.TextInput(attrs={'placeholder': 'Estado'}),
            'district': forms.TextInput(attrs={'placeholder': 'Bairro'}),
            'country': forms.TextInput(attrs={'placeholder': 'País'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '(00) 00000-0000'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email@email.com'}),
            'cnpj': forms.TextInput(attrs={'placeholder': '00.000.000/0000-00'}),
        }
        fields = ['name', 'cnpj', 'email', 'phone_number', 'postal_code', 'street_address', "number", 'city', 'state',
                  'district', 'country']
        labels = {
            'name': ("Nome"),
            'cnpj': ("CNPJ"),
            'email': ("Email"),
            'phone_number': ("Número de telefone"),
            'postal_code': ("CEP"),
            'street_address': ("Nome da rua"),
            'number': ("Número"),
            'city': ("Cidade"),
            'state': ("Estado"),
            'district': ("Bairro"),
            "country": ("País"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].widget.attrs.update({'class': 'mask-phone'})
        self.fields['cnpj'].widget.attrs.update({'class': 'mask-cnpj'})
        self.fields['postal_code'].widget.attrs.update({'class': 'mask-cep'})
        self.fields['street_address'].widget.attrs.update({'class': 'street_address'})
        self.fields['city'].widget.attrs.update({'class': 'city'})
        self.fields['district'].widget.attrs.update({'class': 'district'})
        self.fields['state'].widget.attrs.update({'class': 'state'})
