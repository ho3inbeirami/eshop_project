from .views import * 
from django.urls import path


urlpatterns = [
    path('',HomeView.as_view(), name='home_page'),
    path('about-us/',AboutView.as_view(), name='about_us_page')
]
