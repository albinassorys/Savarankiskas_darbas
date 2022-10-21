from django.db import models

class Cat(models.Model):
    cat_breed = models.CharField('Katės veislė', max_length=200, help_text='Pasirinkite katės veislę')

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
    BREED_TYPE = (
        ('0', 'Šuo'),
        ('1', 'Katė'),
    )
    type = models.CharField(max_length=1, choices=BREED_TYPE, null=False, blank=False,
                            help_text='Pasirinkite gyvūno rūšį')

    cat_breed = models.ForeignKey(Dog, on_delete=models.CASCADE, null=True)
    dog_breed = models.ForeignKey(Cat, on_delete=models.CASCADE, null=True)

    name = models.CharField('Vardas', max_length=200, null=True, help_text='Nurodykite gyvūno vardą')
    STATUS_TYPE = (
        ('0', 'Dingo'),
        ('1', 'Rasta'),
    )
    status = models.CharField(max_length=1, choices=STATUS_TYPE, default='0', help_text='Pasirinkite gyvūno būseną')
    image = models.ImageField('Atvaizdas', null=True, help_text='Įkelkite gyvūno atvaizdą')
    date = models.DateField('Data', null=True, help_text='Nurodykite radimo / dingimo datą', auto_now_add=True)

    def __str__(self):
        return f'{self.type} {self.name}'

    class Meta:
        verbose_name = 'Gyvūnas'
        verbose_name_plural = 'Gyvūnai'