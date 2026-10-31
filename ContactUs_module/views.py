from django.shortcuts import render,redirect
from . import forms
from django.urls import reverse
# Create your views here.
from . import models 

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