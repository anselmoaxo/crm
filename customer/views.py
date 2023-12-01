
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Customer, Contato
from .forms import CustomerForm, ContatoForm
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required


class ListCustomer(ListView):
    template_name = "customer/customer_list.html"
    paginate_by = 10
    model = Customer
    context_object_name = 'customers'

    def get_queryset(self):
        retorno_pesquisa = self.request.GET.get('pesquisa_name')
        if retorno_pesquisa:
            customers = self.model.objects.filter(
               Q(first_name__icontains=retorno_pesquisa) |
               Q(last_name__icontains=retorno_pesquisa)
               )
        else:
            customers = self.model.objects.all()

        return customers
    

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
    
    
class DeleteCustomer(DeleteView):
    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Customer, id=id)
    
    def get_success_url(self):
        return reverse('customer:list')
    


class ListContato(ListView):
    template_name = "customer/contato_list.html"
    paginate_by = 10
    model = Contato
    context_object_name = 'contatos'

    def get_queryset(self):
        retorno_pesquisa = self.request.GET.get('pesquisa_name')
        if retorno_pesquisa:
            contatos = self.model.objects.filter(
               Q(first_name__icontains=retorno_pesquisa) |
               Q(last_name__icontains=retorno_pesquisa)
               )
        else:
            contatos = self.model.objects.all()

        return contatos
    

class CreateContato(CreateView):
    template_name = "customer/contato_create.html"
    form_class = ContatoForm

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('customer:contato_list')
    

class UpdateContato(UpdateView):
    template_name = "customer/contato_create.html"
    form_class = ContatoForm

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Contato, id=id)


    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('customer:contato_list')
    
    
class DeleteContato(DeleteView):
    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Contato, id=id)
    
    def get_success_url(self):
        return reverse('customer:contato_list')
    