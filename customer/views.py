from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Customer
from .forms import CustomerForm
from django.urls import reverse
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
    
    

