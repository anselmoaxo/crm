from typing import Any
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, CreateView,UpdateView
from .models import Customer
from .forms import CustomerForm
from django.urls import reverse
from django.shortcuts import get_object_or_404
# Create your views here.
class ListCustomer(ListView):
    template_name = "customer/customer_list.html"
    model = Customer
    queryset = Customer.objects.all()
    context_object_name = 'customers'


class CreateCustomer(CreateView):
    template_name = "customer/customer_create.html"
    form_class = CustomerForm

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('customer:list')
    

class UpdateCustomer(UpdateView):
    template_name = "customer/customer_create.html"
    form_class = CustomerForm

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Customer, id=id)


    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('customer:list')
    
    

