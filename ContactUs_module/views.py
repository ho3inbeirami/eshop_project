from django.shortcuts import render,redirect
from . import forms
from django.urls import reverse
# Create your views here.
from . import models 
from django.views import View
from django.views.generic.edit import FormView
from django.views.generic import ListView
from . import models
class ContactUsFormView(FormView):
    template_name = 'ContactUs_module/contactus_page.html'
    form_class = forms.ContactUsModelForm
    success_url = '/'
    
    def form_valid(self, form):
        form.save()
        print('form saved !!!')
        return super().form_valid(form)
    



def save_files(f):
    with open('temp/image.png', 'wb+') as des:
        for chunk in f.chunks():
            des.write(chunk)
    print('file saved')



class ContactUsFileUpload(View):
    def get(self,request):
        
        context = {'form':forms.UserProfileForm()}
        return render(request, 'ContactUs_module/upload.html',context)
    
    def post(self,request):
        
        form_data = forms.UserProfileForm(request.POST,request.FILES)
        if form_data.is_valid():
            profile = models.UserProfileModel(image = request.FILES['image'])
            profile.save()
        context = {'form':form_data}
        
        return render(request, 'ContactUs_module/upload.html',context)
        


class ProfileListView(ListView):
    template_name = 'ContactUs_module/profile_list.html'
    model = models.UserProfileModel
    context_object_name = 'profiles'


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