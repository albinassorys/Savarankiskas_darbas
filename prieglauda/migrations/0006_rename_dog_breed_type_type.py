# Generated by Django 4.1.2 on 2022-10-21 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prieglauda', '0005_type_alter_animal_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='type',
            old_name='dog_breed',
            new_name='type',
        ),
    ]
