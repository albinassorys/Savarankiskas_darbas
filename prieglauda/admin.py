from django.contrib import admin
from .models import Animal, Cat, Dog


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('type', 'name')


admin.site.register(Animal)
admin.site.register(Dog)
admin.site.register(Cat)
