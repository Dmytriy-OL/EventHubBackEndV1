from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('feedback/', feedback, name='feedback'),
    path('personal_page/', personal_page, name='personal_page'),
    path('add_new_event/', add_new_event, name='add_new_event'),
    path('event/<slug:event_id>/', show_event, name='show_event')

    # path('events/', eventss),
]
