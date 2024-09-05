from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm, LoginForm

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, "userauths/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Add a successful messages
                messages.success(request, f'Welcome, {username}! You have successfully logged in.')
                return redirect("/")
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            
    else:
        form = LoginForm()
    return render(request, "userauths/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("/")

def home_view(request):
    return render(request, "main/home.html")

