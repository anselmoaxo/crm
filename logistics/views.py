
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Produto, UnidadeMedida
from .forms import ProdutoForm
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required




class ProdutoCreate(CreateView):
    login_url = reverse_lazy('login')
    template_name = 'produto.html'
    form_class = ProdutoForm
    success_url = reverse_lazy('lista_prod')


class ProdutoList(ListView):
    login_url = reverse_lazy('login')
    template_name = 'lista_prod.html'
    model = Produto
    context_object_name = 'produtos'

    def get_queryset(self):
        queryset = super().get_queryset()
        termo_pesquisa = self.request.GET.get("pesquisa", None)
        if termo_pesquisa:
            queryset = queryset.filter(prod_descricao__icontains=termo_pesquisa)
        print(queryset)
        return queryset


class UpdateProduto(UpdateView):
    template_name = "produto.html"
    form_class = ProdutoForm
    success_url = reverse_lazy('lista_prod')

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Produto, id=id)

    
class DeleteProduto(DeleteView):
    model = Produto
    success_url = reverse_lazy("lista_prod")
    
    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Produto, id=id)
