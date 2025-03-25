from django import template
from event.models import *

register = template.Library()

menu = [{'name': 'Add new Event', 'url_name': 'add_new_event'},
        {'name': 'Feedback', 'url_name': 'feedback'},
        # {'name': 'Personal Page', 'url_name': 'personal_page'},
        {'name': 'About Page', 'url_name': 'about'}]


@register.simple_tag
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.simple_tag
def get_events(filter=None):
    if not filter:
        return Event.objects.all()
    else:
        return Event.objects.filter(author__slug=filter)


@register.inclusion_tag('event/partials/category/list_categories.html')
def show_categories(sort=None, selected_category=None):
    if not sort:
        categories = Category.objects.all()
    else:
        categories = Category.objects.order_by(sort)

    return {'categories': categories, 'selected_category': selected_category}


@register.inclusion_tag('event/partials/menu_list.html')
def show_menu():
    return {'menu': menu, }


@register.inclusion_tag('event/partials/cookiepopup.html')
def show_cookiepopup():
    return {}
