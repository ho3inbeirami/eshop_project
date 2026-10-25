from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list_page' ),
    path('products/<slug:slug>', views.product_detail, name='product_detail_page' )
]
