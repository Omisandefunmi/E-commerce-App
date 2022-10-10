from django.shortcuts import render
from django.http import HttpResponse


def get_products(request):
    return HttpResponse("All products")


def landing_page(request):
    return render(request, 'landing_page.html', {'name': 'Bimbo'})
