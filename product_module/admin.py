from django.contrib import admin
from .models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_filter = ['category', 'is_active']
    list_display = ['title', 'price','is_active', 'is_delete']
    list_editable = ['price','is_active']

admin.site.register(Product,ProductAdmin )
admin.site.register(ProductCategory )
admin.site.register(ProductTags )
admin.site.register(Brand)