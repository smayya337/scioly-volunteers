"""scioly_volunteers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.urls import path
from scioly_volunteers.authentication import views, new_views

app_name = "authentication"

urlpatterns = [
    path("", new_views.IndexView.as_view(), name="index"),
    path(
        "login",
        auth_views.LoginView.as_view(template_name="authentication/login.html"),
        name="login",
    ),
    path("register", new_views.register_view, name="register"),
    path("logout", new_views.logout_view, name="logout"),
]
