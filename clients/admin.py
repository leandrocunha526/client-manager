from django.contrib import admin
from .models import Person, Document, Sale, Product

admin.site.register(Person)
admin.site.register(Document)
admin.site.register(Sale)
admin.site.register(Product)
