from django.urls import path

from . import views
from .views import (
    unpublish_product,
    products_by_category_view,
)

app_name = "catalog"

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("product/add/", views.ProductCreateView.as_view(), name="product_add"),
    path("product/<int:pk>/edit/", views.ProductUpdateView.as_view(), name="product_edit"),
    path('product/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path("product/<int:pk>/delete/", views.ProductDeleteView.as_view(), name="product_delete"),
    path("categories/", views.CategoryListView.as_view(), name="category_list"),
    path("contacts/", views.ContactView.as_view(), name="contact"),
    path('products/<int:pk>/unpublish/', unpublish_product, name='unpublish_product'),

    path('', views.ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/unpublish/', views.unpublish_product, name='unpublish_product'),
    path('product/<int:pk>/publish/', views.publish_product, name='publish_product'),
    path("category/<int:category_id>/", products_by_category_view, name="products_by_category"),
]
