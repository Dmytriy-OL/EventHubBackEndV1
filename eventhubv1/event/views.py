from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [{'name': 'Add new Event', 'url_name': 'add_new_event'},
        {'name': 'Feedback', 'url_name': 'feedback'},
        {'name': 'Personal Page', 'url_name': 'personal_page'},
        {'name': 'About Page', 'url_name': 'about'}]


def index(request):
    posts = Event.objects.all()

    print(posts)
    # print(menu[0].values())

    context = {
        'menu': menu,
        'post': posts,
        'title': 'EventHub Main Page'
    }

    return render(request, 'event/index.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'title': 'EventHub About Page'
    }
    return render(request, 'event/about.html', context=context)


def personal_page(request):
    return HttpResponse("<h1>Personal Page</h1>")


def add_new_event(request):
    return HttpResponse("<h1>Add new Event</h1>")


def feedback(request):
    return HttpResponse("<h1>Feedback</h1>")

def show_event(request, event_id):
    return HttpResponse(f"Event which id is {event_id}")

# def eventss(request):
#     return HttpResponse("<h1>event 1</h1><h1>event 2</h1>")
#
#
# def event(request, event_id):
#     # if (request.GET):
#     #     print(request.GET)
#     if (int(event_id) > 10):
#         # raise Http404()
#         return redirect('home', permanent=True)
#
#     return HttpResponse(f"<h1>event - </h1>{event_id}")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page Not Foundddd</h1>")
