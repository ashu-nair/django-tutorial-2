from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("clothing:home")              # <- redirect to clothing home
        else:
            messages.error(request, "Invalid form submission. Please try again.")
    else:
        form = UserCreationForm()

    return render(request, "register/signup.html", {"form": form})


def signin(request):
    if request.method == "POST":
        # pass request in first arg and POST in data= for AuthenticationForm
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("clothing:home")              # <- redirect to clothing home
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, "register/signin.html", {"form": form})


def logout_view(request):
    auth_logout(request)
    return redirect("accounts:signin")                    # or wherever you want logged‑out users to go
