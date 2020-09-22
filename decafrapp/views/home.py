from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from decafrapp.models import DrinkEntry

def home(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            drink_entries = DrinkEntry.objects.all().filter(user=request.user).order_by('-id')[:3]
            template = 'home.html'
            context = {'drink_entries': drink_entries }
            return render(request, template, context) 
    else:
        return redirect('decafrapp:login')