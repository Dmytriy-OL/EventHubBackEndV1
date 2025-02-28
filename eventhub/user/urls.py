from django.urls import path

from user.views import *

urlpatterns = [
    path('users/', users, name='users'),
    path('personal_page/<slug:author_slug>/', personal_page, name='personal_page'),

]
