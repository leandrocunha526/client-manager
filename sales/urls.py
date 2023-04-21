from django.urls import path
from .views import sale_list, DeleteSale, DeleteItemSale, new_sale, item_list, new_item, item_detail, sale_detail, \
    sale_update, item_update, StatsView

urlpatterns = [
    path('list/', sale_list, name='sale-list'),
    path('delete/sale/<int:sale>/', DeleteSale.as_view(), name='delete-sale'),
    path('delete/item/<int:item>/', DeleteItemSale.as_view(), name='delete-item-sale'),
    path('new/', new_sale, name="new-sale"),
    path('item/', new_item, name="new-item"),
    path('item/list', item_list, name="item-list"),
    path('item/detail/<int:id>/', item_detail, name='item-detail'),
    path('detail/<int:id>/', sale_detail, name='sale-detail'),
    path('edit/<int:id>/', sale_update, name='sale-update'),
    path('item/edit/<int:id>/', item_update, name='item-update'),
    path('stats/', StatsView.as_view(), name='stats')
]
