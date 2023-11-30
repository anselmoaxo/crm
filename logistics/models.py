from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class UnidadeMedida(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao


class Produto(models.Model):

    prod_descricao = models.CharField(max_length=100)
    codigo_barra = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    preco = models.FloatField(default=0)
    img_produto = models.ImageField(upload_to= 'img_produto',blank=True, null=True)
    unidade = models.ForeignKey(UnidadeMedida, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.prod_descricao


class EntradaNfe(models.Model):
    descricao = models.CharField(max_length=50, verbose_name=' Descrição da Entrada')
    numero_nfe = models.IntegerField()
    quantidade = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.descricao


class SaidaNfe(models.Model):
    descricao = models.CharField(max_length=50, verbose_name=' Descrição da Saída')
    quantidade = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.descricao


TIPO_MOVIMENTO = (
    ("SAIDAS", "SAIDAS"),
    ("ENTRADA", "ENTRADAS"),
)


class Movimentacao(models.Model):
    tipo = models.CharField(max_length=15, choices=TIPO_MOVIMENTO)
    quantidade = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data = models.DateTimeField(default=timezone.now)
    saldo = models.IntegerField()

    def __str__(self):
        return self.tipo



# Create your models here.
