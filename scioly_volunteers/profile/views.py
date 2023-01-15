from django.http import HttpResponse


def profile(request):
    return HttpResponse("This is your profile!")
