from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from user.models import *


def users(request):
    return HttpResponse("Hello, world. You're at the")


def personal_page(request, author_slug):
    user = get_object_or_404(Author, slug=author_slug)
    # print(user)
    return render(request, 'user/personal_page.html', {'user': user, })
