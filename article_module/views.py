from django.shortcuts import render

# Create your views here.
from .models import Article,ArticleCategory

from django.views.generic import ListView



class ArticleListView(ListView):
    model = Article
    template_name = 'article_module/article_list.html'
    context_object_name = 'Articles'
    paginate_by =1

    
    

    

