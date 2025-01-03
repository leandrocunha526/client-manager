from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Client
from .forms import ClientForm


@login_required
def client_list(request):
    clients = Client.objects.all()
    search = request.GET.get('search')
    if search:
        clients = Client.objects.filter(first_name__icontains=search)
    return render(request, 'clients.html', {'clients': clients, 'search': search})


@login_required
def client_new(request):
    form = ClientForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('client_list')
    return render(request, 'client_form.html', {'form': form})


@login_required
def client_update(request, id):
    client = get_object_or_404(Client, pk=id)
    form = ClientForm(request.POST or None, request.FILES or None, instance=client)

    if form.is_valid():
        form.save()
        return redirect('client_list')
    return render(request, 'client_form.html', {'form': form})


@login_required
def client_delete(request, id):
    client = get_object_or_404(Client, pk=id)

    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'client_delete_confirm.html', {'client': client})


@login_required
def client_detail(request, id):
    client = get_object_or_404(Client, pk=id)
    return render(request, 'client_detail.html', {'client': client})
