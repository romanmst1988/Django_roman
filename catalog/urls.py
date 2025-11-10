from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("product/add/", views.ProductCreateView.as_view(), name="product_add"),
    path(
        "product/<int:pk>/edit/", views.ProductUpdateView.as_view(), name="product_edit"
    ),
    path(
        "product/<int:pk>/delete/",
        views.ProductDeleteView.as_view(),
        name="product_delete",
    ),
    path("categories/", views.CategoryListView.as_view(), name="category_list"),
    path("contacts/", views.ContactView.as_view(), name="contact"),
]
