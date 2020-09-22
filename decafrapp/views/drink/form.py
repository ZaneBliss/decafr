from django.shortcuts import render, redirect
from ..forms import DrinkForm
from decafrapp.models import Drink

def drink_form(request):
    if request.method == 'POST':
        form = DrinkForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
        return redirect('decafrapp:newentry')
    drink_form = DrinkForm()
    template = 'drink/drink_form.html'
    context = {
        "drink_form": drink_form
    }
    return render(request, template, context)

def drink_edit_form(request, pk):
    drink = Drink.objects.get(pk=pk)
    drink_form = DrinkForm(instance=drink)
    
    if request.method == 'POST':
        drink_form = DrinkForm(request.POST or None, instance=drink)
        drink_form.save()
        return redirect('decafrapp:drinks')
        
    template = 'drink/drink_form.html'
    context = {
        'drink': drink,
        'drink_form': drink_form
    }
    return render(request, template, context)