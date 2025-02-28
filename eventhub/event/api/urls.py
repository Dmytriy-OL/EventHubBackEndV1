from django.urls import path

from event.api.views import *


urlpatterns = [
    path('eventlist/', EventListAPIView.as_view()),
    path('event/<int:pk>/', EventDetailAPIView.as_view()),
    path('event/create/', EventCreateAPIView.as_view()),
    path('categorylist/', CategoryListAPIView.as_view()),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view()),
    path('category/create/', CategoryCreateAPIView.as_view()),
]