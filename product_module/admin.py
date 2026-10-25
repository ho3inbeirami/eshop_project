from django.contrib import admin
from .models import Product

# Register your models here.

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price','rating','is_active']
    list_editable = ['price', 'rating', 'is_active']
    prepopulated_fields = {'slug':['title']}
    list_filter = [ 'rating', 'is_active']


admin.site.register(Product, ProductModelAdmin )