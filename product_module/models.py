from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    is_active = models.BooleanField(default= False)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5) ], default=0)
    short_description = models.CharField(max_length=400, null= True)
    
    
    def __str__(self):
        return f'{self.title} ({self.price})'
    
    

