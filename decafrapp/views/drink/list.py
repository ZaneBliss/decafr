from django.shortcuts import render
from decafrapp.models import Drink

def drink_list(request):
    drinks = Drink.objects.all()
    context = { 
        'drinks': drinks
    }
    return render(request, 'drink/drink_list.html', context)