# Generated by Django 4.1.2 on 2022-10-21 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prieglauda', '0008_alter_animal_cat_breed_alter_animal_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='cat_breed',
            field=models.ForeignKey(blank=True, default='Breed', help_text='Pasirinkite katės veislę', null=True, on_delete=django.db.models.deletion.CASCADE, to='prieglauda.cat'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='cat_breed',
            field=models.CharField(default='Foreign', help_text='Pasirinkite katės veislę', max_length=200, verbose_name='Katės veislė'),
        ),
    ]
