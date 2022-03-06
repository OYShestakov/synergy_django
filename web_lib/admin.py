from django.contrib import admin
from web_lib.models import Author, Book, ExtUser, Product, Store


@admin.register(Author)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'email']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'page_count']

@admin.register(ExtUser)
class ExtUserAdmin(admin.ModelAdmin):
    list_display = ['desc', 'is_logged']

    def __str__(self):
        return self.desc

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']

    def __str__(self):
        return self.name

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name']

    def __str__(self):
        return self.name