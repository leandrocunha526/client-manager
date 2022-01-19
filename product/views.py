from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product


@login_required
def products_list(request):
    products = Product.objects.all().order_by('id')
    return render(request, 'product.html', {'product': products})


@login_required
def product_delete(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_delete_confirm.html', {'product': product})
