from django.shortcuts import render
from django.http import HttpResponse
from .models import Animal
from django.views import generic
from django.core.paginator import Paginator


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
