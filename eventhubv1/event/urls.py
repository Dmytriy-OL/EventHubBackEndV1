from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('events/', events),
    path('event/<int:event_id>/', event)
]

