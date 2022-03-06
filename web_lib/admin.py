from django.contrib import admin
from web_lib.models import Author, Book


@admin.register(Author)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'email']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'page_count']