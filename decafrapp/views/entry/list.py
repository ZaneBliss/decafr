from django.shortcuts import render
from decafrapp.models import Drink, Entry, DrinkEntry

def entry_list(request):
    entries = Entry.objects.all()
    drinks = Drink.objects.all()
    drink_entries = DrinkEntry.objects.all() 
    for drink_entry in drink_entries:
        for entry in entries:
            if entry.id == drink_entry.entry_id:
                for drink in drinks:
                    if drink.id == drink_entry.drink_id:
                        entry.drink = drink
    context = { 
        'entries': entries,
    }
    return render(request, 'entry/entry_list.html', context)