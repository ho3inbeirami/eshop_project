from django.shortcuts import render

# Create your views here.
from .models import Article,ArticleCategory

from django.views.generic import ListView
from django.views import View


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
        return render(request, 'article_module/article_detail.html' ,{'single':single})