from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Animal

class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['type', 'breed', 'status', 'name', 'date', 'image']
