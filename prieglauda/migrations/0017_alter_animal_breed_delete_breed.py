# Generated by Django 4.1.2 on 2022-10-23 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prieglauda', '0016_alter_breed_animal_breed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='breed',
            field=models.TextField(default='Mišri', help_text='Pasirinkite gyvūno veislę', max_length=200, verbose_name='Veislė'),
        ),
        migrations.DeleteModel(
            name='Breed',
        ),
    ]
