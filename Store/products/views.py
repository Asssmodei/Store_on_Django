from django.shortcuts import render
from .models import Category, Product


def index(request):
    context = {'title': 'Main title'}
    return render(request, template_name='products/index.html', context=context)


def products(request):
    context = {'title': 'Title',
            'products': Product.objects.all(),
            'category': Category.objects.all()}
    return render(request, template_name='products/products.html', context=context)
