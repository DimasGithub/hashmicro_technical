from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

def custom_login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'auth/login.html')

def index(request):
    context = {
        "name": "Dimas Indra Setiawan",
        "title": "Technical Test"
    }
    return render(request, 'index.html', context)