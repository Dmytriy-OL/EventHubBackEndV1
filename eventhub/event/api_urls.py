from django.urls import path

from event.api_views import EventAPIView


urlpatterns = [
    path('api/v1/eventlist/', EventAPIView.as_view()),

]