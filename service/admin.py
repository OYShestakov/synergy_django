from django.contrib import admin

from .models import Product, Bin

# admin.site.register(Product)
admin.site.register(Bin)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'coast']
    fields = ['id']
    list_filter = ['coast']
    search_fields = ['title']

# admin.site.register(Product, ProductAdmin)
