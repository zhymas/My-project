from .views import *
from django.urls import path,include

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact', contact, name='contacts'),

]