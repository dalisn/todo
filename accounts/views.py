from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from accounts.forms import LoginForm, RegistrationForm
from lists.forms import TodoForm

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login_view(request):
    print("Login view accessed.")
    if request.method == "POST":
        print("POST request received.")
        form = LoginForm(request.POST)
        if form.is_valid():
            print("Form is valid.")
            user = authenticate(
                username=request.POST["username"], password=request.POST["password"]
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    print(f"User {user.username} logged in successfully.")
                    return redirect("lists:overview")  # Redirect to lists overview
                else:
                    print("User account is not active.")
            else:
                print("Authentication failed.")
        else:
            print("Form is not valid.")
        return render(request, "accounts/login.html", {"form": form})
    else:
        return render(request, "accounts/login.html", {"form": LoginForm()})


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=request.POST["username"],
                email=request.POST["email"],
                password=request.POST["password"],
            )
            return redirect("auth:login")
        else:
            return render(request, "accounts/register.html", {"form": form})
    else:
        return render(request, "accounts/register.html", {"form": RegistrationForm()})


def logout_view(request):
    logout(request)
    return redirect("lists:index")
