from django.shortcuts import render, redirect
from .forms import DrinkForm

def drink(request):
    if request.method == 'GET':
        drink_form = DrinkForm()
        context = {
            "drink_form": drink_form
        }
        return render(request, "drink_form.html", context)

    if request.method == 'POST':
        form = DrinkForm(request.POST or None)
        if form.is_valid():
            form.save()
        
        return redirect("decafrapp:newentry")