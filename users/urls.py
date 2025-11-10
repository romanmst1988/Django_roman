from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import ProductCreateView, ProductUpdateView, RegisterView, CustomLoginView

app_name = "users"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="products_list"), name="logout"),
    path("profile/edit/", ProductCreateView.as_view(), name="profile_edit"),
]
