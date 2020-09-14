from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect

# Create your views here.
from django.views import View


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home.html")


def Signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully created!')
            return redirect(reverse("login"))
        else:
            form = UserCreationForm()
            return render(request, "signup.html", {"form": form})
    else:
        form = UserCreationForm()
        return render(request, "signup.html", {"form": form})

