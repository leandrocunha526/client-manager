from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category
from .forms import ProductForm, CategoryForm


@login_required
def product_list(request):
    products = Product.objects.all().order_by('id')
    search = request.GET.get('search')
    if search:
        products = Product.objects.filter(name__icontains=search)
    return render(request, 'product.html', {'product': products, 'search': search})


@login_required
def product_delete(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_delete_confirm.html', {'product': product})


@login_required
def product_new(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'product_form.html', {'form': form})


@login_required
def product_update(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'product_form.html', {'form': form})


@login_required
def category_new(request):
    form = CategoryForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'category_form.html', {'form': form})


@login_required
def category_list(request):
    category = Category.objects.all().order_by('id')
    search = request.GET.get('search')
    if search:
        category = Category.objects.filter(name__icontains=search)
    return render(request, 'category.html', {'category': category, 'search': search})


@login_required
def category_delete(request, id):
    category = get_object_or_404(Category, pk=id)

    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category_delete_confirm.html', {'category': category})


@login_required
def category_update(request, id):
    category = get_object_or_404(Category, pk=id)
    form = CategoryForm(request.POST or None, instance=category)

    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'category_form.html', {'form': form})


@login_required
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'product_detail.html', {'product': product})
