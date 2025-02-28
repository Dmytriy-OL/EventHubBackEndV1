from django.urls import path

from event.api.api_views import *


urlpatterns = [
    path('eventlist/', EventListAPIView.as_view()),
    path('event/<int:pk>/', EventDetailAPIView.as_view()),
]