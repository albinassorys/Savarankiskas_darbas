# Generated by Django 4.1.2 on 2022-10-23 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prieglauda', '0015_breed_remove_animal_cat_breed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='animal_breed',
            field=models.TextField(default='Mišri', help_text='Pasirinkite gyvūno veislę', max_length=200, verbose_name='Veislė'),
        ),
    ]
