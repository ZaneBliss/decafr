from django.shortcuts import render, redirect
from django.contrib import messages
from decafrapp.models import Entry, Drink, DrinkEntry
from ..forms import EntryForm, DrinkEntryForm

def entry_form(request):
    drink_entry_form = DrinkEntryForm(user=request.user)
    entry_form = EntryForm()
    drinks = Drink.objects.all()

    if request.method == 'POST':
        form = EntryForm(request.POST or None)
        if form.is_valid():
            form.save()
            selected_drink = Drink.objects.get(pk=form.data['drink'])
            latest_entry = Entry.objects.latest('id')
            DrinkEntry.objects.create(
                user=request.user,
                drink_id=selected_drink.id, 
                entry_id=latest_entry.id
            )
            return redirect('decafrapp:entries')
        else:
            messages.error(request, form.errors)
            return redirect(request.path_info)

    template = 'entry/entry_form.html'
    context = { 
        "drinks": drinks,
        "entry_form": entry_form,
        "drink_entry_form": drink_entry_form
    }
    return render(request, template, context)

def entry_edit_form(request, pk):
    drink_entry = DrinkEntry.objects.get(entry_id=pk)
    entry  = drink_entry.entry
    drink = drink_entry.drink
    entry_form = EntryForm(instance=entry)
    
    if request.method == 'POST':
        entry_form = EntryForm(request.POST or None, instance=entry)
        entry_form.save()
        return redirect('decafrapp:entries')
        
    template = 'entry/entry_form.html'
    context = {
        'drink': drink,
        'entry': entry,
        'entry_form': entry_form
    }
    return render(request, template, context)