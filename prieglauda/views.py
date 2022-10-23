from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Animal
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from .forms import CreateOrderForm
from django.contrib import messages


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

@csrf_protect
def sign_up(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:

            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('sign_up')
            else:

                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('sign_up')
                else:

                    messages.success(request, ('Prisiregistravote sėkmingai'))
                    User.objects.create_user(username=username, email=email, password=password)

        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('sign_up')
    return render(request, 'registration/sign_up.html')


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
