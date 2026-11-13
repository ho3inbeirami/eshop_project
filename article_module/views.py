from django.shortcuts import render

# Create your views here.
from .models import Article,ArticleCategory, ArticleComments

from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse

class ArticleListView(ListView):
    model = Article
    template_name = 'article_module/article_list.html'
    context_object_name = 'Articles'
    paginate_by =5
    ordering = ['id']

    def get_queryset(self):
        cat = self.kwargs.get('category')
        if cat:
            queryset = super().get_queryset()
            queryset = queryset.filter(selected_categories__url_title = cat)
            return queryset
        return super().get_queryset()
    
    
    

def article_category_component(request):
    main_categories = ArticleCategory.objects.filter(is_active=True,parent_id =None)
    context = {'main_categories': main_categories}
    
    return render(request, 'article_module/article_category_component.html', context)
    


class ArticleDetailView(View):
    def get(self,request,pk):
        single = Article.objects.filter(id = pk, is_active=True).first()
        context = {
            'single':single,
            'main_comments':ArticleComments.objects.filter(article_id =pk,parent_id=None).order_by('-created_date').prefetch_related('parent')
            }
        
        return render(request, 'article_module/article_detail.html' ,context)
    
    
    


def add_article_comment(request: HttpResponse):
    
    if request.user.is_authenticated:
        
        comment = request.GET.get('comment')
        article_id = request.GET.get('article_id')
        parent = request.GET.get('parent_id')
        print(parent)
        obj = ArticleComments(message=comment, article_id = article_id , user = request.user , parent_id = parent)
        obj.save()
        context = {
            'main_comments':ArticleComments.objects.filter(article_id =article_id,parent_id=None).order_by('-created_date').prefetch_related('parent'),
            
        }
        return  render(request,'article_module/includes/comment_box.html',context)
    
    return  HttpResponse("")