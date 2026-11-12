from django.urls import path
from . import views
urlpatterns = [
    path('articles/<int:pk>',views.ArticleDetailView.as_view() ,name= 'article_detail_page'),
    path('articles/',views.ArticleListView.as_view() ,name= 'articles_page'),

    path('articles/<str:category>',views.ArticleListView.as_view() , name='articles_by_category_page'),
    
]
