from django.utils.crypto import get_random_string
from django.http import HttpResponseRedirect, Http404, HttpRequest
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from .models import User
from . import forms
from django.contrib.auth import login, logout
from utils import email_service



class RegisterView(View):
    def get(self,request):
        form = forms.RegisterForm()
        context = {'form':form}
        return render(request, 'account_module/register_page.html',context)
    
    def post(self,request):
        form = forms.RegisterForm(request.POST)
        
        if form.is_valid():
            # user does exist in database 
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            has_user: bool = User.objects.filter(email__iexact=email).exists()
            
            if has_user:
                form.add_error('email','the user is duplicate')
                context = {'form':form}
                return render(request, 'account_module/register_page.html', context)
            
            else:
                user = User(username = email,email = email, is_active=False, email_active_code = get_random_string(72))
                user.set_password(password)
                user.save()
                # todo : send email activation code
                                
                email_service.Send_email('activation Email',user.email, {'user':user} , 'emails/active-account.html' )

                
                return HttpResponseRedirect(reverse('login_page'))
        
        # if form is not valid
        context = {'form':form}
        return render(request, 'account_module/register_page.html', context)




class LoginView(View):
    
    def get(self, request):
        
        form = forms.LoginForm()
        context = {'form':form}
        return render(request, 'account_module/login_page.html', context)
    
    def post(self, request:HttpRequest):
        form  = forms.LoginForm(request.POST)
        context = {'form':form}
        
        if form.is_valid():
            user_email =  form.cleaned_data.get('email')
            user_pass = form.cleaned_data.get('password')
            user = User.objects.filter(email__iexact= user_email).first()
            
            if user:
                if user.check_password(user_pass) and user.is_active:
                    # login 
                    login(request,user)
                    return HttpResponseRedirect(reverse('home_page'))
                else:
                    #wrong password
                    form.add_error('password','login data is invalid')
                    
                    context = {'form':form}
                    return render(request, 'account_module/login_page.html', context)
            else:
                #email does not exist
                form.add_error('email','user does not exist')
                context = {'form':form}
                return render(request, 'account_module/login_page.html', context)
        
        else:
            # form dat a is in valid
            return render(request, 'account_module/login_page.html', context)



class ActivateAccountView(View):
    def get(self,request,email_active_code):
        user = User.objects.filter(email_active_code__iexact = email_active_code).first()
        
        
        if user is not None:
            user.is_active = True
            user.email_active_code = get_random_string(72)
            user.save()
            return HttpResponseRedirect(reverse('login_page'))
        
        else:
            raise Http404()



class ForgetPassWordView(View):
    
    def get(self,request: HttpRequest):
        form = forms.ForgetPassWordForm()
        return render(request , 'account_module/forget_pass_page.html',{'form':form})
        
    def post(self,request: HttpRequest):

        form = forms.ForgetPassWordForm(request.POST)
        user_email =request.POST.get('email')
        user = User.objects.filter(email__iexact=user_email).first()
        
        if user:
            user.email_active_code
            # to do send Email To user
            email_service.Send_email('activation Email',user.email, {'user':user} , 'emails/forget-pass.html' )
            return render(request , 'account_module/forget_pass_page.html',{'form':form,'message':'Email Was sent to user'})
        else:
            return HttpResponseRedirect(reverse('register_page'))
        
        
        
class SetPasswordView(View):
    def get(self,request, email_active_code):
        form = forms.SetPassWordForm()
        return render(request , 'account_module/set_password_page.html', {'form':form})
    
    def post(self,request: HttpRequest, email_active_code: str):
        user:User = User.objects.filter(email_active_code__iexact = email_active_code).first()
        
        if user:
            user_password = request.POST.get()
            user.set_password('password')
            user.email_active_code=get_random_string(72)
            user.save()
            return  HttpResponseRedirect(reverse('login_page'))
        
        raise Http404()
    
    
class LogoutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse('login_page'))