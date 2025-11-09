from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from .models import User
from .forms import UserRegisterForm, EmailAuthenticationForm
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('products:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        # send welcome email
        send_mail(
            subject='Welcome to the Shop',
            message=f'Hello {self.object.username}, thanks for registering.',
            from_email=None,  # uses DEFAULT_FROM_EMAIL
            recipient_list=[self.object.email],
            fail_silently=True,
        )
        # auto-login the user
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(self.request, email=self.object.email, password=raw_password)
        if user:
            login(self.request, user)
        return response

class CustomLoginView(LoginView):
    authentication_form = EmailAuthenticationForm
    template_name = 'users/login.html'

class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'email', 'avatar', 'phone', 'country']
    template_name = 'users/profile_edit.html'
    success_url = reverse_lazy('products:list')

    def get_object(self, queryset=None):
        return self.request.user
