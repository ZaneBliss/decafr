from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def home(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'home.html') 
    else:
        return redirect('decafrapp:login')