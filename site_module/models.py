from django.db import models

# Create your models here.



class SiteSettings(models.Model):

    site_name = models.CharField(max_length=200, verbose_name='Site Name')
    site_url = models.CharField(max_length=200, verbose_name='Site Url')
    about_us = models.TextField(verbose_name='About Us')
    address = models.TextField(verbose_name='Address')
    telephone = models.CharField(max_length=200,null=True, blank=True, verbose_name='Telephone')
    fax = models.CharField(max_length=200, null=True, blank=True, verbose_name= 'Fax')
    email = models.CharField(max_length=200,null=True, blank=True, verbose_name= 'Email')
    copyright = models.TextField(verbose_name='Copyright')
    site_logo = models.FileField(upload_to='images/site-setting', verbose_name='Site Logo',null=True)
    is_main_setting = models.BooleanField(default=False, verbose_name='Main Setting')
        
    def __str__(self):
        return self.site_name
    
    class Meta:
        db_table = 'SiteSetting'
        verbose_name = 'Site Setting'
        verbose_name_plural = 'Site Settings'
        
        
        
class FooterBox(models.Model):
    title = models.CharField(max_length=200, verbose_name='Footer Box')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Footer box'
        verbose_name_plural = 'Footer boxes'
        

class FooterBoxLink(models.Model):
    title = models.CharField(max_length=200, verbose_name='Footer Box title')
    link = models.URLField("", max_length=200)
    footer_box = models.ForeignKey(FooterBox,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Footer link'
        verbose_name_plural = 'Footer links'