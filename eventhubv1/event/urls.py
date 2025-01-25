from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('feedback/', feedback, name='feedback'),
    path('personal_page/', personal_page, name='personal_page'),
    path('add_new_event/', add_new_event, name='add_new_event'),
    path('event/<int:event_id>/', show_event, name='show_event'),
    # path('event/<slug:event_name>/', show_event, name='show_event'),
    path('category/<int:category_id>/', show_category, name='show_category')

    # path('events/', eventss),
]
