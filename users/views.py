from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
# попробую иначе
from django.views.generic.edit import FormView

from catalog.forms import ProductForm
from catalog.models import Product
from .forms import EmailAuthenticationForm
from .forms import UserRegisterForm
from .models import User

'''Тут-та и начал по новой'''
class RegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в магазин недвижимости'
        message = 'Спасибо, что зарегистрировались в нашем магазине недвижимости!'
        from_email = 'romain.mst.python@yandex.ru'
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)

class CustomLoginView(LoginView):
    authentication_form = EmailAuthenticationForm
    template_name = "users/login.html"
#
#
class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ["username", "email", "avatar", "phone", "country"]
    template_name = "users/profile_edit.html"
    success_url = reverse_lazy("home")

    def get_object(self, queryset=None):
        return self.request.user

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

