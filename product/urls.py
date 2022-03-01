from django.urls import path
from .views import product_list, product_delete, product_new, product_update, category_new, category_list, \
    category_update, category_delete, product_detail


urlpatterns = [
    path('list/', product_list, name="product_list"),
    path('delete/<int:id>', product_delete, name="product_delete"),
    path('new/', product_new, name="product_new"),
    path('update/<int:id>', product_update, name="product_update"),
    path('detail/<int:id>', product_detail, name="product_detail"),
    path('category/new/', category_new, name="category_new"),
    path('category/list/', category_list, name="category_list"),
    path('category/update/<int:id>', category_update, name="category_update"),
    path('category/delete/<int:id>', category_delete, name="category_delete"),
]
