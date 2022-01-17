from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registrado com sucesso")
            return redirect("home")
        messages.error(request, "Informações inválidas")
    form = NewUserForm()
    return render(request=request, template_name="register_form.html", context={"form": form})
