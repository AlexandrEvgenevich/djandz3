from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    sort_val = 'name'

    if sort == 'name':
        sort_val = 'name'
    if sort == 'min_price':
        sort_val = '-price'
    if sort == 'max_price':
        sort_val = 'price'

    phones = Phone.objects.order_by(sort_val)
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    pho = Phone.objects.filter(slug=slug)
    context = {
        'phone': pho[0]
    }
    return render(request, template, context)
