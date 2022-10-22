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
        fields = ['type', 'cat_breed', 'dog_breed', 'name', 'date']


# class EditUserAccountForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['email', 'image']