from django.urls import path
from .views import main, rasta, dingo, sign_up, create_order, order_detail

urlpatterns = [
    path('', main, name='main'),
    path('rasta/', rasta, name='rasta'),
    path('dingo/', dingo, name='dingo'),
    path('registration/sign_up', sign_up, name='sign_up'),
    path('create_order/', create_order, name='create_order'),
    path('order_detail<int:id>/', order_detail, name='order_detail')]


