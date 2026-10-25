from django.shortcuts import render
from .models import Product
# Create your views here.

def product_list(request):
    products_list = Product.objects.all()
    context = {'products_list': products_list}
    return render(request, 'product_module/product_list.html',context=context)



def product_detail(request, slug ):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
        }
    return render(request, 'product_module/product_detail.html',context=context)