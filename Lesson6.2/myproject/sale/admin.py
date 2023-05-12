from django.contrib import admin
from .model import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    list_filter = ('price',)
    search_fields = ('name', 'description')

admin.site.register(Product, ProductAdmin)