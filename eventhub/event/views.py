from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

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
    allow_empty = False

    def get_context_data(self, **kwargs, ):
        context = super().get_context_data(**kwargs)
        context['selected_category'] = context['events'][0].category_id
        return context

    def get_queryset(self):
        events = Event.objects.filter(category__slug=self.kwargs['category_slug'])
        return events


def about(request):
    context = {
        'title': 'EventHub About Page'
    }
    return render(request, 'event/about.html', context=context)


class AddEventView(CreateView):
    form_class = EventForm
    template_name = 'event/add_page.html'
    extra_context = {'title': 'Add Event'}


class EditEventView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'event/edit_page.html'
    slug_field = 'slug'
    slug_url_kwarg = 'event_slug'

    def get_success_url(self):
        return reverse_lazy('show_event', kwargs={'event_slug': self.object.slug})


def feedback(request):
    return HttpResponse("<h1>Feedback</h1>")


class ShowEventView(DetailView):
    model = Event
    template_name = 'event/event_page.html'
    slug_url_kwarg = 'event_slug'
    # extra_context = {'title': 'EventHub Main Page', 'selected_category': 0}


def delete_event(request, event_slug):
    event = get_object_or_404(Event, slug=event_slug)
    event.delete()
    return redirect('home')


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page Not Found</h1><h2>Please try again</h2>")

def privacy_policy(request):
    return render(request, "event/privacy-policy.html")