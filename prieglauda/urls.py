from django.urls import path, include
from .views import main, rasta, dingo

urlpatterns = [
    path('', main, name='main'),
    path('rasta/', rasta, name='rasta'),
    path('dingo', dingo, name='dingo')]


