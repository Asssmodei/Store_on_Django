from django.urls import path
from products.views import products

app_name = 'products'# обязательная переменная!

urlpatterns = [
    path('', products, name='index')
]
