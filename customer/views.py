from django.shortcuts import render
from django.views.generic import ListView
from .models import Customer

# Create your views here.
class ListCustomer(ListView):
    template_name = "customer/customer_list.html"
    model = Customer
    queryset = Customer.objects.all()
    context_object_name = 'customers'

