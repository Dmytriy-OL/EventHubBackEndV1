from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = ["Main Page", "Add new Event", "Feedback", "Personal Page"]


def index(request):
    posts = Event.objects.all()
    print(posts)
    return render(request, 'event/index.html', { 'menu': menu, 'post': posts, 'title': 'EventHub Main Page'})


def about(request):
    return render(request, 'event/about.html', {'menu': menu, 'title': 'EventHub About Page'})


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
