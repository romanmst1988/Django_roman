from django.urls import path

from . import views

# app_name = 'catalog'

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("contacts/", views.contacts, name="contacts"),
    path('contact/', views.contact_view, name='contact'),
    path('contact/post/', views.contact_post, name='contact_post'),
    path('real_estate_catalog/', views.real_estate_catalog, name='real_estate_catalog'),
]
