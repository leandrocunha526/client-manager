from django.forms import ModelForm
from .models import Client


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'age', 'salary', 'biography', 'photo']
        labels = {
            'first_name': ("Primeiro nome"),
            'last_name': ("Sobrenome"),
            'age': ("Idade"),
            'salary': ("Salário"),
            'biography': ("Biografia"),
            'photo': ("Foto")
        }
