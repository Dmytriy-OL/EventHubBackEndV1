from django.urls import path

from user.api.views import *

urlpatterns = [
    path('userlist/', AuthorListAPIView.as_view()),
    path('user/<int:pk>/', AuthorDetailAPIView.as_view()),
]
