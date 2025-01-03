from django.urls import path
from clients.views import client_delete, client_detail, client_list, client_new, client_update

urlpatterns = [
    path('list/', client_list, name="client_list"),
    path('new/', client_new, name="client_new"),
    path('update/<int:id>/', client_update, name="client_update"),
    path('delete/<int:id>/', client_delete, name="client_delete"),
    path('detail/<int:id>/', client_detail, name="client_detail")
]
