from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('prod_descricao','codigo_barra','unidade', 'quantidade','preco','img_produto')