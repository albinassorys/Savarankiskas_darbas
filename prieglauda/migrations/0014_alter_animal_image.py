# Generated by Django 4.1.2 on 2022-10-22 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prieglauda', '0013_alter_animal_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='image',
            field=models.ImageField(help_text='Įkelkite gyvūno atvaizdą', null=True, upload_to='', verbose_name='Atvaizdas'),
        ),
    ]
