from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.


def welcome(request):
    return render(request, 'user_accounts/welcome.html', {})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been Logged in..."))
            return redirect('storehome')
        else:
            messages.success(
                request, ("Username or Password incorrect...Please try again"))
            return redirect('login_user')
    else:
        return render(request, 'user_accounts/login.html', {'title': 'Sign in'})


def logout_user(request):
    logout(request)
    messages.success(request, ('Logged out...Thank you!'))
    return redirect('login_user')
