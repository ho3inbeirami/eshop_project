from django.contrib.auth.models import AbstractUser

from django.db import models

class User(AbstractUser):
    mobile = models.CharField(max_length=10,verbose_name='mobile', null=True, blank=True)
    email_active_code = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=False,null=False, blank=False)
    
    class Meta:
        db_table = 'Users'
        verbose_name = 'user'
        verbose_name_plural ='users'