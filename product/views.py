from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm


@login_required
def product_list(request):
    products = Product.objects.all().order_by('id')
    return render(request, 'product.html', {'product': products})


@login_required
def product_delete(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_delete_confirm.html', {'product': product})


@login_required
def product_new(request):
    form = ProductForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'product_form.html', {'form': form})


@login_required
def product_update(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'product_form.html', {'form': form})