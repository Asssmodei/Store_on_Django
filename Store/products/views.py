from django.shortcuts import render
from .models import Category, Product


def index(request):
    context = {'title': 'Что происходит?'}
    return render(request, template_name='products/index.html', context=context)


def products(request):
    context = {'title': 'Ya samy pizdatui',
            'products': Product.objects.all(),
            'category': Category.objects.all()}
    return render(request, template_name='products/products.html', context=context)
