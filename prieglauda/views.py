from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Animal
from django.contrib.auth import login
from django.views import generic
from django.core.paginator import Paginator
from .forms import SignUpForm, CreateOrderForm


# class AnimalView(generic.ListView):
#     model = Animal
#     paginate_by = 9
#     template_name = 'main.html'


def main(request):
    # paginator = Paginator(Animal.objects.all(), 2)
    # page_number = request.GET.get('page')
    # paged_animals = paginator.get_page(page_number)
    # context = {
    #     'animals': paged_animals
    # }
    animals = Animal.objects.all()
    context = {
        'animals': animals
    }

    return render(request, 'main.html', context=context)


def dingo(request):
    # paginator = Paginator(Animal.objects.all(), 2)
    # page_number = request.GET.get('page')
    # paged_animals = paginator.get_page(page_number)
    # context = {
    #     'animals': paged_animals
    # }
    animals = Animal.objects.filter(status__exact='1')
    context = {
        'animals': animals
    }

    return render(request, 'main.html', context=context)


def rasta(request):
    # paginator = Paginator(Animal.objects.all(), 2)
    # page_number = request.GET.get('page')
    # paged_animals = paginator.get_page(page_number)
    # context = {
    #     'animals': paged_animals
    # }
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
            return redirect('create_order_detail', id=order.id)
    else:
        form = CreateOrderForm()
    return render(request, 'create_order.html', context={'form': form})