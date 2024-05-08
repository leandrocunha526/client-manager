from django.urls import path
from .views import supplier_form, supplier_list, supplier_update, supplier_delete, supplier_detail

urlpatterns = [
    path('new/', supplier_form, name="supplier-form"),
    path('list/', supplier_list, name="supplier-list"),
    path('delete/<int:id>', supplier_delete, name="supplier-delete"),
    path('update/<int:id>', supplier_update, name="supplier-update"),
    path('detail/<int:id>', supplier_detail, name="supplier-detail")
]
