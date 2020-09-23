from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm

def register(request):
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'registration/register.html', {'form':form})

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user =  authenticate(username=username, password=password)
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, 'Submission rejected. Please ensure you meet form requirements.')
            return redirect(request.path_info)