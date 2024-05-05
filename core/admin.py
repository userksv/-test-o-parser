from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'image_url', 'discount']

admin.site.register(Product, ProductAdmin)