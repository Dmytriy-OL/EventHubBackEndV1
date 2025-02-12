from django.urls import path

from event.api.api_views import *


urlpatterns = [
    path('api/v1/eventlist/', EventListAPIView.as_view()),
    path('api/v1/event/<int:pk>/', EventDetailAPIView.as_view()),
]