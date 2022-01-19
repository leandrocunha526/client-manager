from django.urls import path
from .views import products_list, product_delete


urlpatterns = [
    path('list/', products_list, name="product_list"),
    path('delete/<int:id>', product_delete, name="product_delete")
]
