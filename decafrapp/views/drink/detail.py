from decafrapp.models import Drink
from django.shortcuts import redirect, reverse

def drink_detail(request, pk):
    form_data = request.POST
    if ('delete' in form_data):
        drink = Drink.objects.get(pk=pk)
        drink.delete()
    return redirect('/drinks')