from django import forms
from . import models

class ContactUsForm(forms.Form):
    email = forms.EmailField(
        label='Email address',
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Email',
                'class':'form-control'
                }
            )
        
        )
    
    full_name = forms.CharField(
        label='Full name',
        widget= forms.TelInput(
            attrs={
                'placeholder':'Full name',
                'class':'form-control'
            }
        )
        )
    title = forms.CharField(
        label='Title',
        widget= forms.TelInput(
            attrs={
                'placeholder':'Subject',
                'class':'form-control'
            }
        )
        
        )
    message = forms.CharField(
        label= 'Your message',
        error_messages={'required':'in field elzamie'} ,
        widget= forms.Textarea(
            attrs={
                'placeholder':'your message',
                'class':'form-control',
                'id':'message'
                }
            )
        
        )
    
    
    
class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = models.ContactUs
        fields = ['email','full_name','title','text']
        widgets = {
            'email':forms.EmailInput(attrs={
                'placeholder':'Email',
                'class':'form-control'
            }),
            
            'full_name':forms.TextInput(attrs={
                'placeholder':'Full name',
                'class':'form-control'
            }),
            
            
            'title':forms.TextInput(attrs={
                'placeholder':'Full name',
                'class':'form-control'
            }),
            
            'text':forms.TextInput(attrs={
                'placeholder':'Your message',
                'class':'form-control',
                'id':'message'
            }),           
        }
    
