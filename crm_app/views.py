from django.http import HttpResponse
from django.shortcuts import render, redirect
from crm_app.models import *
from crm_app.forms import OrderForm

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


def createOrder(request):

    form = OrderForm()

    if request.method == 'POST':
        # print('Printing Post:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'crm_app/order_form.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'crm_app/order_form.html', context)


def deleteOrder(request, pk):

    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'crm_app/delete.html', context)
