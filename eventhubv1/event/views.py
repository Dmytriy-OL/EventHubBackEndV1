from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *


def index(request):
    events = Event.objects.all()

    context = {
        'events': events,
        'title': 'EventHub Main Page',
        'selected_category': 0

    }
    return render(request, 'event/index.html', context=context)


def show_category(request, category_id):
    events = Event.objects.filter(category_id=category_id)

    if len(events) == 0:
        raise Http404

    context = {
        'events': events,
        'selected_category': category_id
    }

    return render(request, 'event/index.html', context=context)


def about(request):
    context = {
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
    return HttpResponseNotFound("<h1>Page Not Found</h1><h2>Please try again</h2>")
