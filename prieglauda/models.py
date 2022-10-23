from django.db import models

class Animal(models.Model):
    ANIMAL_TYPE = (
        ('1', 'Šuo'),
        ('2', 'Katė'),
    )
    type = models.CharField('Rūšis', max_length=1, choices=ANIMAL_TYPE, null=False, blank=False,
                              help_text='Pasirinkite gyvūno rūšį')

    breed = models.CharField('Veislė', max_length=200, help_text='Pasirinkite gyvūno veislę', editable=True, null=True, default='Mišri')

    name = models.CharField('Vardas', max_length=200, null=True, help_text='Nurodykite gyvūno vardą', default='Be vardo')
    STATUS_TYPE = (
        ('1', 'Dingo'),
        ('2', 'Rasta'),
    )
    status = models.CharField('Būsena', max_length=1, choices=STATUS_TYPE, default='0', help_text='Pasirinkite gyvūno būseną')
    image = models.ImageField('Atvaizdas', upload_to='', null=True, help_text='Įkelkite gyvūno atvaizdą')
    date = models.DateField('Data', null=True, help_text='Nurodykite radimo / dingimo datą', editable=True)

    def __str__(self):
        return f'{self.get_type_display()} {self.name}'

    class Meta:
        verbose_name = 'Gyvūnas'
        verbose_name_plural = 'Gyvūnai'

