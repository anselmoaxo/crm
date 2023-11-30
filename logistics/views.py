from .forms import ProdutoForm
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Produto, EntradaNfe, SaidaNfe, Movimentacao
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.db import transaction
from django.db.models import Q




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

# Create your views here.
