from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            authorized = True
            return render(request, 'index.html')
        else:
            messages.success(request, 'Invalid Username or Password')
            return render(request, 'login.html')
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return render(request, 'logout.html')







