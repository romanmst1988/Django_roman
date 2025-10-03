from django.urls import path
from catalog import views
from . import views

# app_name = 'catalog'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('contact_post/', views.contact_post, name='contact_post'),
]