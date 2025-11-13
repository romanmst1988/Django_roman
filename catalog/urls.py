from django.urls import path

from . import views
from .views import (
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    unpublish_product,
)


app_name = "catalog"

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("product/add/", views.ProductCreateView.as_view(), name="product_add"),
    path("product/<int:pk>/edit/", views.ProductUpdateView.as_view(), name="product_edit"),
    path("product/<int:pk>/delete/", views.ProductDeleteView.as_view(), name="product_delete"),
    path("categories/", views.CategoryListView.as_view(), name="category_list"),
    path("contacts/", views.ContactView.as_view(), name="contact"),
    path('products/<int:pk>/unpublish/', unpublish_product, name='unpublish_product'),
]
