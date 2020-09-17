from decafrapp.models import Entry, DrinkEntry
from django.shortcuts import redirect, reverse

def entry_detail(request, pk):
    form_data = request.POST
    if ('delete' in form_data):
        entry = Entry.objects.get(pk=pk)
        drink_entry = DrinkEntry.objects.get(entry_id=entry.id)
        drink_entry.delete()
    return redirect('/entries')