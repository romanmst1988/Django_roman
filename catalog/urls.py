from django.urls import path  # type: ignore
from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('contact_post/', views.contact_post, name='contact_post'),
]