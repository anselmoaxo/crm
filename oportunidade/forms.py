from django import forms
from .models import Oportunidade


class OportunidadeForm(forms.ModelForm):
    class Meta:
        model = Oportunidade
        fields = ['cliente', 'descricao', 'valor_estimado', 'data_fechamento', 'status']

        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),  # Lista de clientes
            'data_fechamento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # Widget de data
        }
