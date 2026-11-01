from django.urls import path
from .views import *


urlpatterns = [
    path('contact-us/',ContactUsFormView.as_view(), name='ContactUs_page')
]
