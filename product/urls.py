from django.urls import path
from .views import product_list, product_delete, product_new, product_update


urlpatterns = [
    path('list/', product_list, name="product_list"),
    path('delete/<int:id>', product_delete, name="product_delete"),
    path('new/', product_new, name="product_new"),
    path('update/<int:id>', product_update, name="product_update"),
]
