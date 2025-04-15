from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg bg-light fs-6',
            'placeholder': 'Username',
            'required': True
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-lg bg-light fs-6',
            'placeholder': 'Email Address',
            'required': True
        })
    )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg bg-light fs-6',
            'placeholder': 'Password',
            'required': True
        })
    )
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg bg-light fs-6',
            'placeholder': 'Confirm Password',
            'required': True
        })
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

# UserLoginForm giữ nguyên như cũ
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg bg-light fs-6',
            'placeholder': 'Username',
            'required': True
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg bg-light fs-6',
            'placeholder': 'Password',
            'required': True
        })
    )