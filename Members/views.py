from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def login_user(request):
    if request.method == 'POST':
        request.session['username'] = request.POST.get('username')
        request.session['password'] = request.POST.get('password')
        username = request.session.get('username')
        password = request.session.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            authorized = True
            context = {'authorized': True}
            return render(request, 'index.html', context)
        else:
            messages.success(request, 'Invalid Username or Password')
            return render(request, 'login.html')
    if request.user.is_authenticated:
        context = {'authorized': True}
        return render(request, 'index.html', context)
    else:
        return render(request, 'login.html')


def logout_user(request):
    request.session.flush()
    request.session.clear_expired()
    logout(request)
    return render(request, 'logout.html')










