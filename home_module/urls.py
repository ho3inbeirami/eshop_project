from .views import * 
from django.urls import path


urlpatterns = [
    path('',index_page, name='home_page')
]
