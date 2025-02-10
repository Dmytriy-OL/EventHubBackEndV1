from django.urls import path, include

from .views import *

urlpatterns = [
    path('', EventHomeView.as_view(), name='home'),
    path('about/', about, name='about'),
    path('feedback/', feedback, name='feedback'),
    path('add_new_event/', add_new_event, name='add_new_event'),
    path('edit/<slug:event_slug>/', edit_event, name='edit_event'),
    path('event/<slug:event_slug>/', show_event, name='show_event'),
    path('delete/<slug:event_slug>/', delete_event, name='delete_event'),
    path('category/<slug:category_slug>/', EventHomeCategoryView.as_view(), name='show_category'),
    path('', include('event.api.api_urls')),
]
