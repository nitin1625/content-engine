from django.http import HttpResponse
from django.urls import path


def home_page(request):
    return HttpResponse("Hello World")