from django import forms
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class':'',
                'placeholder':'Email'
            }
        )
    )
    
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'',
                'placeholder':'Password'
            }
        )
    )
    confirm_password =forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'',
                'placeholder':'Confirm Password'
            }
        )


    )
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        
        if password == confirm_password:
            return confirm_password
        
        raise ValidationError('password and confirm password most be unique')


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class':'',
                'placeholder':'Email'
            }
        )
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'',
                'placeholder':'Password'
            }
        )
    )



class ForgetPassWordForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class':'',
                'placeholder':'Email'
            }
        )
    )
    
    
    
class SetPassWordForm(forms.Form):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'',
                'placeholder':'Password'
            }
        )
    )
    confirm_password =forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'',
                'placeholder':'Confirm Password'
            }
        )
    )