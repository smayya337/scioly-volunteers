from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello!")


def login(request):
    return HttpResponse("Success!")


def register(request):
    return HttpResponse("Welcome!")


def logout(request):
    return HttpResponse("Goodbye!")
