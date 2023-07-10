from django.urls import path

from catalog.views import home, contacts, orders, categories

urlpatterns = [
    path('', home, name='home'),
    path('home', home, name='home'),
    path('categories', categories, name='categories'),
    path('orders', orders, name='orders'),
    path('contacts', contacts, name='contacts')
]
