from django.db import models

from account_module.models import User
# Create your models here.


class ArticleCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title')
    url_title = models.CharField(max_length=300, verbose_name='Url Title', unique=True)
    is_active = models.BooleanField(default=True, verbose_name='Active / de Active')
    parent =models.ForeignKey('ArticleCategory', on_delete=models.CASCADE, verbose_name='parent Category', null=True,blank=True, related_name='sub_categories')
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name ='Article category'
        verbose_name_plural = 'Article Categories'
        db_table = 'ArticlesCategory'

class Article(models.Model):
    title = models.CharField(max_length=200,verbose_name='Title')
    short_description = models.TextField(null=True,blank=True,  verbose_name = 'short description')
    description = models.TextField(null=True,blank=True, verbose_name = 'description')
    slug = models.SlugField(max_length=300, allow_unicode=True,verbose_name='Url_title', default=' ')
    image = models.ImageField(upload_to='uploads/images/articles', null=True)
    is_active= models.BooleanField(verbose_name='active / deactive', default=True)
    selected_categories = models.ManyToManyField(ArticleCategory, verbose_name='Category')
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='author', null=True, blank=True)
    datetime = models.DateTimeField(verbose_name='datatime', auto_now_add=True)
    rating = models.PositiveIntegerField(verbose_name='rating', default=1)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'Articles'
        verbose_name ='Article'
        verbose_name_plural = 'Articles'
        
        
    
    
class ArticleComments(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name='Article',related_name='ArticleComment')
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='user')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    parent = models.ForeignKey('ArticleComments',on_delete=models.CASCADE,verbose_name='Parent Article',null=True, blank=True, related_name='sub_comments')
    message = models.TextField(verbose_name='message')
    
    def __str__(self):
        return f'{self.article.title} ({self.user})'
    class Meta:
        
        db_table = 'ArticleComments'
        verbose_name ='ArticleComment'
        verbose_name_plural = 'ArticleComments'
        
        
    
    