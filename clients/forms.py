from django.forms import ModelForm
from .models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age', 'salary', 'biography', 'photo']
        labels = {
            'first_name': ("Primeiro nome"),
            'last_name': ("Segundo nome"),
            'age': ("Idade"),
            'salary': ("Salário"),
            'biography': ("Biografia"),
            'photo': ("Foto")
        }
