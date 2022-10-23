from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Animal
from django.contrib.auth import login
from .forms import SignUpForm, CreateOrderForm


def main(request):
    animals = Animal.objects.all()
    context = {
        'animals': animals
    }

    return render(request, 'main.html', context=context)


def dingo(request):
    animals = Animal.objects.filter(status__exact='1')
    context = {
        'animals': animals
    }

    return render(request, 'main.html', context=context)


def rasta(request):
    animals = Animal.objects.filter(status__exact='2')
    context = {
        'animals': animals
    }

    return render(request, 'main.html', context=context)


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('create_order')
    else:
        form = SignUpForm()
    return render(request, 'registration/sign_up.html', context={'form': form})


@login_required()
def create_order(request):
    if request.method == 'POST':
        request_data = request.POST.copy()
        request_data['user'] = request.user.id
        form = CreateOrderForm(request_data, request.FILES)
        if form.is_valid():
            order = form.save()
            return redirect('order_detail', id=order.id)
    else:
        form = CreateOrderForm()
    return render(request, 'create_order.html', context={'form': form})


def order_detail(request, id):
    order_details = Animal.objects.filter(id=id).all()
    context = {
        'order_details': order_details
    }
    return render(request, 'order_detail.html', context=context)
