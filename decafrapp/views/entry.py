from django.shortcuts import render, redirect
from decafrapp.models import Entry, Drink
from .forms import EntryForm

def entry(request):
    if request.method == 'GET':
        form = EntryForm()
        drinks = Drink.objects.all()
        context = { 
            "drinks": drinks,
            "form": form
        }
        return render(request, 'entry_form.html', context)

    if request.method == 'POST':
        form = EntryForm(request.POST or None)
        if form.is_valid():
            form.save()

        return redirect("decafrapp:home")