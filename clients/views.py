from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from .forms import PersonForm


@login_required
def persons_list(request):
    persons = Person.objects.all()
    search = request.GET.get('search')
    if search:
        persons = Person.objects.filter(first_name__icontains=search)
    return render(request, 'person.html', {'persons': persons, 'search': search})


@login_required
def persons_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')
    return render(request, 'person_delete_confirm.html', {'person': person})


@login_required
def person_detail(request, id):
    person = get_object_or_404(Person, pk=id)
    return render(request, 'person_detail.html', {'person': person})
