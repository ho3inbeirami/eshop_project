from django.shortcuts import render
from .models import Product

from django.db.models import Avg
from django.views.generic import ListView, DeleteView
from . import models

# Create your views here.


class ProductListView(ListView):
    model = models.Product
    template_name = 'product_module/product_list.html'
    context_object_name ='products_list'
    
    paginate_by =2

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset  # TODO
        return queryset




def product_list(request):
    products_list = Product.objects.all().order_by('-price')
    context = {
        'products_list': products_list,
        'count':Product.objects.count(),
        'AVG':Product.objects.aggregate(Avg('price'))
        }
    return render(request, 'product_module/product_list.html',context=context)



class ProductDetailView(DeleteView):
    template_name = 'product_module/product_detail.html'
    model = Product
    context_object_name = 'product'

def product_detail(request, slug ):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
        }
    return render(request, 'product_module/product_detail.html',context=context)