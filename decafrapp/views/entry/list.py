from django.shortcuts import render
from decafrapp.models import Drink, Entry, DrinkEntry

def entry_list(request):
    entries = Entry.objects.all()
    drink_entries = DrinkEntry.objects.all().filter(user=request.user)
    context = { 
        'drink_entries': drink_entries
    }
    return render(request, 'entry/entry_list.html', context)