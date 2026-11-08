from django.contrib import admin
from . import models
# Register your models here.

class SliderModelAdmin(admin.ModelAdmin):
    list_display = ['title','image','url','url_title','is_active']
    list_editable = ['image','url','url_title','is_active']


admin.site.register(models.Slider,SliderModelAdmin)