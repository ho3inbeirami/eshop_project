from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    is_active = models.BooleanField(default= False)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5) ]
        , default=0)
    short_description = models.CharField(max_length=400, null= True)

    slug= models.SlugField(default='', null=False,unique=True)
    
    
    def get_absolute_url(self):
        return reverse("product_detail_page", kwargs={ 'slug':self.slug} )
    
    def __str__(self):
        return f'{self.title} ({self.price})'
    
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    

 