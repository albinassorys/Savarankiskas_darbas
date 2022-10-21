# Generated by Django 4.1.2 on 2022-10-21 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prieglauda', '0002_alter_animal_cat_breed_alter_animal_dog_breed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='cat_breed',
            field=models.ForeignKey(help_text='Pasirinkite katės veislę', null=True, on_delete=django.db.models.deletion.CASCADE, to='prieglauda.cat'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='dog_breed',
            field=models.ForeignKey(help_text='Pasirinkite šuns veislę', null=True, on_delete=django.db.models.deletion.CASCADE, to='prieglauda.dog'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='type',
            field=models.CharField(choices=[('0', 'Šuo'), ('1', 'Katė')], help_text='Pasirinkite gyvūno rūšį', max_length=1, verbose_name='Rūšis'),
        ),
    ]