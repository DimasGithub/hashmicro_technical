from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import render

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

def handler404(request, exception=None):
    response = render(request, 'oops.html',
                      {'title': '404 Not Found', 'message': '404'})
    response.status_code = 404
    return response


def handler403(request, exception=None):
    response = render(request, 'oops.html',
                      {'title': '403 Permission Denied', 'message': '403'})
    response.status_code = 403
    return response

def handler400(request, exception=None):
    response = render(request, 'oops.html',
                      {'title': '400 Bad Request', 'message': '400'})
    response.status_code = 400
    return response

def handler500(request, exception=None):
    print("sds")
    response = render(request, 'oops.html',
                      {'title': '500 Bad Request', 'message': '500'})
    response.status_code = 500
    return response
