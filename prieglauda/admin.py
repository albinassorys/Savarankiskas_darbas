from django.contrib import admin
from .models import Animal


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('type', 'name')


admin.site.register(Animal)