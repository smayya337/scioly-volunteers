from django.http import HttpResponse


def userpage(request, username):
    return HttpResponse(f"This is the userpage for {username}")
