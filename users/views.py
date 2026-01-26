from django.contrib.auth import logout
from django.shortcuts import redirect
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


'''для кнопок'''
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

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

