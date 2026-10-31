from django.db import models

# Create your models here.


class ContactUs(models.Model):
    email = models.EmailField(max_length=200)
    full_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    is_read_by_admin = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    response = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'ContactUs'
        verbose_name = 'Contact Us form'
        verbose_name_plural = 'Contact Us forms'