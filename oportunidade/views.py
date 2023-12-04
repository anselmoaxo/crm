
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Oportunidade
from .forms import OportunidadeForm
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required




class OportunidadeCreate(CreateView):
    login_url = reverse_lazy('login')
    template_name = 'oportunidade.html'
    form_class =  OportunidadeForm
    success_url = reverse_lazy('oportunidade:oportunidade_list')


class OportunidadeList(ListView):
    login_url = reverse_lazy('login')
    template_name = 'card_oportunidade.html'
    model = Oportunidade
    context_object_name = 'oportunidades'

    def get_queryset(self):
        queryset = super().get_queryset()
        termo_pesquisa = self.request.GET.get("pesquisa", None)
        if termo_pesquisa:
            queryset = queryset.filter(descricao__icontains=termo_pesquisa)
        print(queryset)
        return queryset


# Create your views here.
