from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    avatar = forms.ImageField(required=False)
    phone = forms.CharField(required=False)
    country = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2', 'avatar', 'phone', 'country')

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email')
