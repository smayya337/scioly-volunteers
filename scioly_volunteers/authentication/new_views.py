from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView

from scioly_volunteers.authentication.forms import RegisterForm


class IndexView(TemplateView):
    template_name = "authentication/index.html"


def register_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You have successfully registered!")
            return redirect(reverse("authentication:index"))
    else:
        form = RegisterForm()

    return render(request, "authentication/register.html", {"form": form})


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect(reverse("authentication:index"))
