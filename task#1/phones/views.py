from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    pnone_objects = Phone.objects.all()
    phones = [f'{c.name}, {c.price}, {c.image}, {c.slug}' for c in pnone_objects]
    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
