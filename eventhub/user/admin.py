from django.contrib import admin

from user.models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'slug', 'avatar')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Author, AuthorAdmin)
