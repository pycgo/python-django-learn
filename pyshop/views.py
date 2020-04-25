from django.http import HttpResponse


def index_view(response):
    return HttpResponse("hello world")