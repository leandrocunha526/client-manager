from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from supplier.forms import SupplierForm
from supplier.models import Supplier


@login_required
def supplier_form(request):
    form = SupplierForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('supplier-list')
    return render(request, 'supplier-form.html', {'form': form})


@login_required
def supplier_list(request):
    supplier = Supplier.objects.all().order_by('id')
    search = request.GET.get('search')
    if search:
        supplier = Supplier.objects.filter(name__icontains=search)
    return render(request, 'supplier.html', {'supplier': supplier, 'search': search})


@login_required
def supplier_delete(request, id):
    supplier = get_object_or_404(Supplier, pk=id)

    if request.method == 'POST':
        supplier.delete()
        return redirect('supplier-list')
    return render(request, 'supplier-confirm.html', {'supplier': supplier})


@login_required
def supplier_update(request, id):
    supplier = get_object_or_404(Supplier, pk=id)
    form = SupplierForm(request.POST or None, instance=supplier)

    if form.is_valid():
        form.save()
        return redirect('supplier-list')
    return render(request, 'supplier-form.html', {'form': form})


@login_required
def supplier_detail(request, id):
    supplier = get_object_or_404(Supplier, pk=id)
    return render(request, 'supplier-detail.html', {'supplier': supplier})
