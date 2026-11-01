from django.shortcuts import render
from django.views .generic import TemplateView
# Create your views here.


def index_page(request):
    return render(request,'home_module/index.html')

class HomeView(TemplateView):
    template_name = 'home_module/index.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['data'] = 'this data is sent to home page'
        return context

def header_component(request):
    return render(request, 'shared/header_component.html')


def footer_component(request):
    return render(request, 'shared/footer_component.html')