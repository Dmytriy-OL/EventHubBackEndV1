from django import template
from event.models import *

register = template.Library()

menu = [{'name': 'Add new Event', 'url_name': 'add_new_event'},
        {'name': 'Feedback', 'url_name': 'feedback'},
        {'name': 'Personal Page', 'url_name': 'personal_page'},
        {'name': 'About Page', 'url_name': 'about'}]


@register.simple_tag
def get_categories(filter=None):
    if not filter:
        return EventCategory.objects.all()
    else:
        return EventCategory.objects.filter(pk=filter)


@register.inclusion_tag('event/list_categories.html')
def show_categories(sort=None, selected_category=None):
    if not sort:
        categories = EventCategory.objects.all()
    else:
        categories = EventCategory.objects.order_by(sort)

    return {'categories': categories, 'selected_category': selected_category}


@register.inclusion_tag('event/menu_list.html')
def show_menu():
    return {'menu': menu, }
