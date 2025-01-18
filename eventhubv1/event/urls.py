from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    # path('events/', eventss),
    # path('event/<int:event_id>/', event)
]

