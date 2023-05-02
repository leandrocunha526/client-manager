from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from sales.forms import SaleForm, ItemForm
from sales.models import Sale, Item
from django.contrib.auth.decorators import login_required
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from django.http import HttpResponse


def generate_pdf(request, id):
    sale = Sale.objects.get(id=id)
    item = Item.objects.get(sales_id=id)
    data = [["Detalhes da venda"],
    ["Código da venda", sale.id],
    ["Imposto", sale.tax],
    ["Total", sale.total],
    ["Desconto", sale.discount],
    ["Criado em", sale.datetime],
    ["Código do cliente", sale.person.id],
    ["Itens", item.products.name],
    ["Cliente", sale.person.first_name + ' ' + sale.person.last_name],
    ["Status", sale.status]]

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="data.pdf"'

    pdf = SimpleDocTemplate(
        response,
        pagesizes=A4
    )

    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 50),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 50),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ]))

    elements = []
    elements.append(table)
    pdf.build(elements)

    return response


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
        sales = Sale.objects.filter(status__icontains=search)
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
