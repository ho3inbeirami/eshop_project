from django.db import models

# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=200,verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.FileField(upload_to='images/sliders',verbose_name='Image')
    url = models.URLField(verbose_name='URL')
    url_title = models.CharField(max_length=200,verbose_name='Url_title')
    is_active = models.BooleanField(verbose_name='active/deactive')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'