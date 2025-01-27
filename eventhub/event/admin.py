from django.contrib import admin

from .models import *


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'authorId', 'image', 'data', 'category')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'category')
    list_editable = ('category',)
    list_filter = ('category', 'data')
    prepopulated_fields = {'slug': ('name',)}
    # list_per_page = 2
    # list_max_show_all = 4


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Event, EventAdmin)
admin.site.register(Category, CategoryAdmin)
