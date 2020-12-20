from django.shortcuts import render
from django.http import HttpResponse

from math import ceil
from .models import Product

# Create your views here.


def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))

    params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'products': products}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("contact page")


def tracker(request):
    return HttpResponse("tracker page")


def search(request):
    prod_list = Product.objects.all()
    print(type(prod_list))
    return HttpResponse(prod_list)
    # return HttpResponse("search page")


def productView(request):
    return HttpResponse("product view page")


def checkout(request):
    return HttpResponse("checkout page")

