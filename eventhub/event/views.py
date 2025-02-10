from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.generic import ListView

from .forms import *
from .models import *


class EventHomeView(ListView):
    model = Event
    template_name = 'event/index.html'
    context_object_name = 'events'

    # extra_context = {'title': 'EventHub Main Page', 'selected_category': 0}

    def get_context_data(self, **kwargs, ):
        context = super().get_context_data(**kwargs)
        context['title'] = 'EventHub Main Page'
        context['selected_category'] = 0
        return context


class EventHomeCategoryView(ListView):
    model = Event
    template_name = 'event/index.html'
    context_object_name = 'events'

    def get_context_data(self, **kwargs, ):
        context = super().get_context_data(**kwargs)
        context['selected_category'] = context['events'][0].category_id
        return context

    def get_queryset(self):
        events = Event.objects.filter(category__slug=self.kwargs['category_slug'])
        if events.exists():
            return events
        else:
            raise Http404


def about(request):
    context = {
        'title': 'EventHub About Page'
    }
    return render(request, 'event/about.html', context=context)


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

    return render(request, 'event/edit_page.html', {'event_slug': event_slug, 'form': form, 'title': 'Edit Event'})


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


def delete_event(request, event_slug):
    event = get_object_or_404(Event, slug=event_slug)
    event.delete()
    return redirect('home')


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page Not Found</h1><h2>Please try again</h2>")
