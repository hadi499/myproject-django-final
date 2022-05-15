from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def loginView(request):
    context = {
        'page_title': 'LOGIN',
    }
    user = None
    if request.method == "POST":

        username_login = request.POST['username']
        password_login = request.POST['password']

        user = authenticate(request, username=username_login,
                            password=password_login)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password is incorrect')
            return redirect('login')

    return render(request, 'users/login.html', context)


def logoutView(request):
    context = {
        'page_title': 'logout'
    }

    if request.method == "POST":
        if request.POST["logout"] == "Submit":
            logout(request)

        return redirect('login')

    return render(request, 'users/logout.html', context)
