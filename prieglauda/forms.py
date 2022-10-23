from django import forms
from django.contrib.auth.forms import UserCreationForm, User
from .models import Animal


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['type', 'breed', 'status', 'name', 'date', 'image']
