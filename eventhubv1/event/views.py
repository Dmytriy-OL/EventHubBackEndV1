from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [{'name': 'Add new Event', 'url_name': 'add_new_event'},
        {'name': 'Feedback', 'url_name': 'feedback'},
        {'name': 'Personal Page', 'url_name': 'personal_page'},
        {'name': 'About Page', 'url_name': 'about'}]


def index(request):
    posts = Event.objects.all()
    category = EventCategory.objects.all()

    context = {
        'menu': menu,
        'post': posts,
        'category': category,
        'title': 'EventHub Main Page',
        'selected_category': 0

    }

    return render(request, 'event/index.html', context=context)


def show_category(request, category_id):
    posts = Event.objects.filter(category_id=category_id)
    category = EventCategory.objects.all()

    if category_id > len(category):
        raise Http404

    context = {
        'menu': menu,
        'post': posts,
        'category': category,
        'title': category[category_id - 1],
        'selected_category': category_id

    }

    # category = EventCategory.objects.all()
    # print(category)
    # return HttpResponse(f"Category which id is {category_id}"
    #                     f"Category name is {category[category_id - 1]}")
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
    return HttpResponseNotFound("<h1>Page Not Found</h1><h2>Please try again</h2>")
