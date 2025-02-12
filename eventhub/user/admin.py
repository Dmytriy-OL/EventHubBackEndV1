from django.contrib import admin

from user.models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname','name', 'surname', 'slug', 'avatar', 'banner')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('nickname',)}


admin.site.register(Author, AuthorAdmin)
