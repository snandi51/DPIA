from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from Assessment import views

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            messages.success(request, 'Invalid Username or Password')
            return render(request, 'login.html')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'You are now logged out')
    return render(request, 'login.html')







