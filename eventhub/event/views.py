from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views import View

from .forms import *
from .models import *


def index(request):
    events = Event.objects.all()

    context = {
        'events': events,
        'title': 'EventHub Main Page',
        'selected_category': 0

    }
    return render(request, 'event/index.html', context=context)


def show_category(request, category_slug):
    events = get_list_or_404(Event, category__slug=category_slug)

    for event in events:
        category_id = event.category.id
        break

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
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                form.add_error(None, "Error adding event")
    else:
        form = EventForm()
    return render(request, 'event/addpage.html', context={'title': 'Add New Event', 'form': form})


def edit_event(request, event_slug):
    event = get_object_or_404(Event, slug=event_slug)
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect(reverse('show_event', kwargs={'event_slug': event.slug}))
    else:
        form = EventForm(instance=event)

    return render(request, 'event/edit_page.html', {'event_slug': event_slug ,'form': form, 'title': 'Edit Event'})


def feedback(request):
    return HttpResponse("<h1>Feedback</h1>")


def show_event(request, event_slug):
    event = get_object_or_404(Event, slug=event_slug)

    context = {
        'event': event,
        'title': event.name,
        'selected_category': event.category_id
    }
    return render(request, 'event/event_page.html', context=context)


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
