from django.urls import path
from . import views
urlpatterns = [
    path('articles/',views.ArticleListView.as_view() ,name= 'articles_page'),
    path('articles/<category>',views.ArticleListView.as_view() , name='articles_by_category_page')
]
