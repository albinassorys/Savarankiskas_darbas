from django.db import models
from django.contrib.auth.models import AbstractUser

class Cat(models.Model):
    cat_breed = models.CharField('Katės veislė', max_length=200, help_text='Pasirinkite katės veislę', default='Mišri')

    def __str__(self):
        return self.cat_breed

    class Meta:
        verbose_name = 'Katės veislė'
        verbose_name_plural = 'Kačių veislės'


class Dog(models.Model):
    dog_breed = models.CharField('Šuns veislė', max_length=200, help_text='Pasirinkite šuns veislę')

    def __str__(self):
        return self.dog_breed

    class Meta:
        verbose_name = 'Šuns veislė'
        verbose_name_plural = 'Šunų veislės'


class Animal(models.Model):
    ANIMAL_TYPE = (
        ('1', 'Šuo'),
        ('2', 'Katė'),
    )
    type = models.CharField('Rūšis', max_length=1, choices=ANIMAL_TYPE, null=False, blank=False,
                              help_text='Pasirinkite gyvūno rūšį')

    cat_breed = models.ForeignKey(Cat, on_delete=models.CASCADE, null=True, blank=True,
                                  help_text='Pasirinkite katės veislę', default='Mišri')
    dog_breed = models.ForeignKey(Dog, on_delete=models.CASCADE, null=True, blank=True,
                                  help_text='Pasirinkite šuns veislę')

    name = models.CharField('Vardas', max_length=200, null=True, help_text='Nurodykite gyvūno vardą')
    STATUS_TYPE = (
        ('1', 'Dingo'),
        ('2', 'Rasta'),
    )
    status = models.CharField('Būsena', max_length=1, choices=STATUS_TYPE, default='0', help_text='Pasirinkite gyvūno būseną')
    image = models.ImageField('Atvaizdas', null=True, help_text='Įkelkite gyvūno atvaizdą')
    date = models.DateField('Data', null=True, help_text='Nurodykite radimo / dingimo datą', auto_now_add=True)

    def __str__(self):
        return f'{self.get_type_display()} {self.name}'

    class Meta:
        verbose_name = 'Gyvūnas'
        verbose_name_plural = 'Gyvūnai'


# class User(AbstractUser):
#     image = models.ImageField(null=True, blank=True)