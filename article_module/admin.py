from django.contrib import admin

# Register your models here.
from . import models

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display= ['title','url_title','is_active','parent']
    list_editable = ['url_title','is_active','parent']

admin.site.register(models.ArticleCategory, ArticleCategoryAdmin)





class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug','is_active']
    list_editable = [ 'slug','is_active',]
    
    def save_model(self, request, obj, form, change):
        if request.user.is_authenticated:
            if change:
                obj.author = request.user
                
        return super().save_model(request, obj, form, change)
    
admin.site.register(models.Article,ArticleAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['article__title', 'user','message','parent']
    #list_editable = [ 'slug','is_active',]

admin.site.register(models.ArticleComments, ArticleAdmin)