from django.http import HttpResponse


def browse(request):
    return HttpResponse("Browsing!")
