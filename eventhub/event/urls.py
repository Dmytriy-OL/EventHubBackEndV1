from django.urls import path

from .views import *

urlpatterns = [
    path('', EventHomeView.as_view(), name='home'),
    path('about/', about, name='about'),
    path('feedback/', feedback, name='feedback'),
    path('add_new_event/', AddEventView.as_view(), name='add_new_event'),
    path('edit/<slug:event_slug>/', EditEventView.as_view(), name='edit_event'),
    path('event/<slug:event_slug>/', ShowEventView.as_view(), name='show_event'),
    path('delete/<slug:event_slug>/', delete_event, name='delete_event'),
    path('category/<slug:category_slug>/', EventHomeCategoryView.as_view(), name='show_category'),
]
