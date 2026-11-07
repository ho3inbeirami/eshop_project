from django.contrib import admin
from . import models
# Register your models here.
#

admin.site.register(models.SiteSettings)

admin.site.register(models.FooterBox)
admin.site.register(models.FooterBoxLink)