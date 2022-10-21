from django.shortcuts import render
from django.http import HttpResponse
from .models import Animal, Cat, Dog


def main(request):
    return render(request, 'main.html')
