from django.http import HttpResponse
from django.shortcuts import render
from crm_app.models import *

# Create your views here.


def index(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()

    delivered = orders.filter(status='Delivered').count()

    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers,
               'total_orders': total_orders, 'delivered': delivered,
               'pending': pending}

    return render(request, 'crm_app/dashboard.html', context)


def products(request):
    products = Product.objects.all()
    return render(request, 'crm_app/product.html', {'products': products})


def customer(request, pk):
    customer = Customer.objects.get(id=pk)

    # Grabbing Customer child object in the (Order) Model
    orders = customer.order_set.all()

    order_count = orders.count()

    context = {'customer': customer,
               'orders': orders, 'order_count': order_count}
    return render(request, 'crm_app/customer.html', context)
