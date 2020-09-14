from django.shortcuts import render, redirect

def home(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'home.html') 
    else:
        return redirect('accounts/login')