from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from sales.forms import SaleForm, ItemForm
from sales.models import Sale, Item
from django.contrib.auth.decorators import login_required


class StatsView(View):
    def dispatch(self, request, *args, **kwargs):
        return super(StatsView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        data = {}
        data['total__avg'] = Sale.objects.media()
        data['discount__avg'] = Sale.objects.media_discount()
        data['tax__avg'] = Sale.objects.media_tax()
        data['min'] = Sale.objects.min()
        data['max'] = Sale.objects.max()
        data['num_sale'] = Sale.objects.number_sale()

        return render(request, 'stats.html', data)


@login_required
def sale_list(request):
    sales = Sale.objects.all().order_by('id')
    search = request.GET.get('search')
    if search:
        sales = Sale.objects.filter(datetime__icontains=search)
    return render(request, 'sale-list.html', {'sales': sales})


class DeleteSale(View):
    def get(self, request, sale):
        sale = Sale.objects.get(id=sale)
        return render(
            request, 'delete-sale-confirm.html', {'sale': sale}
        )

    def post(self, request, sale):
        sale = Sale.objects.get(id=sale)
        sale.delete()
        return redirect('sale-list')


class DeleteItemSale(View):
    def get(self, request, item):
        item = Item.objects.get(id=item)
        return render(
            request, 'delete-item-confirm.html', {'item': item}
        )

    def post(self, request, item):
        item = Item.objects.get(id=item)
        item.delete()
        return redirect('item-list')


@login_required
def new_sale(request):
    form_sale = SaleForm(request.POST or None)
    if form_sale.is_valid():
        form_sale.save()
        return redirect('sale-list')
    return render(request, 'new-sale.html', {'form_sale': form_sale})


@login_required
def new_item(request):
    form_item = ItemForm(request.POST or None)
    if form_item.is_valid():
        form_item.save()
        return redirect('sale-list')
    return render(request, 'items.html', {'form_item': form_item})


@login_required
def item_list(request):
    items = Item.objects.all()
    search = request.GET.get('search')
    if search:
        items = Item.objects.filter(products__name__icontains=search)
    return render(request, 'items-list.html', {'items': items})


@login_required
def item_detail(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'item-detail.html', {'item': item})


@login_required
def sale_detail(request, id):
    sale = get_object_or_404(Sale, pk=id)
    return render(request, 'sale-detail.html', {'sale': sale})


@login_required
def sale_update(request, id):
    sale = get_object_or_404(Sale, pk=id)
    form_sale = SaleForm(request.POST or None, instance=sale)

    if form_sale.is_valid():
        form_sale.save()
        return redirect('sale-list')
    return render(request, 'new-sale.html', {'form_sale': form_sale})


@login_required
def item_update(request, id):
    item = get_object_or_404(Item, pk=id)
    form_item = ItemForm(request.POST or None, instance=item)

    if form_item.is_valid():
        form_item.save()
        return redirect('item-list')
    return render(request, 'items.html', {'form_item': form_item})
