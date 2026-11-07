from django.shortcuts import render,redirect
from . import forms
from django.urls import reverse
# Create your views here.
from . import models 
from django.views import View
from django.views.generic.edit import FormView
from django.views.generic import ListView
from . import models
from site_module.models import SiteSettings
class ContactUsFormView(FormView):
    template_name = 'ContactUs_module/contactus_page.html'
    form_class = forms.ContactUsModelForm
    success_url = '/'
    
    def form_valid(self, form):
        form.save()
        print('form saved !!!')
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site = SiteSettings.objects.filter(is_main_setting=True).first()
        context["site"] = site
        return context
    



class ContactUsView(View):
    def get(self,request):
        contact_form = forms.ContactUsModelForm()
        context  = {'contact_form':contact_form}
        return render(request, 'ContactUs_module/contactus_page.html',context)
    
    def post(self,request):
        contact_form = forms.ContactUsModelForm(request.POST)
        if contact_form.is_valid():
            print(contact_form.cleaned_data)
            contact_form.save()
            return redirect(reverse('home_page'))
        else:
            context  = {'contact_form':contact_form}
            return render(request, 'ContactUs_module/contactus_page.html',context)





def ContactUs(request):
    if request.method == "POST":
        #contact_form = forms.ContactUsForm(request.POST)
        contact_form = forms.ContactUsModelForm(request.POST)
        if contact_form.is_valid():
            print(contact_form.cleaned_data)
            # data = models.ContactUs(
            #     email=contact_form.cleaned_data.get('email'),
            #     full_name = contact_form.cleaned_data.get('full_name'),
            #     title= contact_form.cleaned_data.get('title'),
            #     text = contact_form.cleaned_data.get('text')
            # )
            # data.save()
            contact_form.save()
            return redirect(reverse('home_page'))
        else:
            context  = {'contact_form':contact_form}
            return render(request, 'ContactUs_module/contactus_page.html',context)
    #contact_form = forms.ContactUsForm()
    contact_form = forms.ContactUsModelForm()
    
    
    context  = {'contact_form':contact_form}
    return render(request, 'ContactUs_module/contactus_page.html',context)