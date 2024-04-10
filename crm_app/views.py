from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'crm_app/dashboard.html')


def product(request):
    return render(request, 'crm_app/product.html')


def customer(request):
    return render(request, 'crm_app/customer.html')
