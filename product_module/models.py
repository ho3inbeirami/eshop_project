from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class ProductCategory(models.Model):
    title = models.CharField(max_length=200,verbose_name='عنوان')
    url_title = models.CharField(max_length=200, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'ProductCategories'
        verbose_name = 'ProductCategory'
        verbose_name_plural = 'ProductCategories'


class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.ManyToManyField(
        ProductCategory, 
        related_name='product_categories')
    
    price = models.IntegerField(verbose_name='price')
    short_description = models.CharField(max_length=400, null= True)
    description = models.TextField(max_length=400)
    slug= models.SlugField(default='', null=False,unique=True, db_index=True)
    is_active = models.BooleanField(default= False)    
    is_delete = models.BooleanField(default=False)
        
    def get_absolute_url(self):
        return reverse("product_detail_page", kwargs={ 'slug':self.slug} )
    
    def __str__(self):
        return f'{self.title} ({self.price})'
    
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'Products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'





class ProductTags(models.Model):
    title = models.CharField(max_length=200,verbose_name='عنوان')
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    class Meta:
        db_table = 'Tags'
        verbose_name = 'Product Tag'
        verbose_name_plural = 'Product Tags'
        
    def __str__(self):
        return self.title