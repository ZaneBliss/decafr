from django.shortcuts import render, redirect
from decafrapp.models import Entry, Drink, DrinkEntry
from .forms import EntryForm, DrinkEntryForm

def entry(request):
    if request.method == 'GET':
        drink_entry_form = DrinkEntryForm()
        entry_form = EntryForm()
        drinks = Drink.objects.all()
        context = { 
            "drinks": drinks,
            "entry_form": entry_form,
            "drink_entry_form": drink_entry_form
        }
        return render(request, 'entry_form.html', context)

    if request.method == 'POST':
        form = EntryForm(request.POST or None)
        if form.is_valid():
            form.save()
            selected_drink = Drink.objects.get(pk=form.data["drink"])
            latest_entry = Entry.objects.latest("date")
            DrinkEntry.objects.create(
                drink_id=selected_drink, 
                entry_id=latest_entry
            )

        return redirect("decafrapp:newentry")