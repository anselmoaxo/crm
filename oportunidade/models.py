
from django.db import models
from customer.models import Customer


class Oportunidade(models.Model):
    cliente = models.ForeignKey(Customer, on_delete=models.CASCADE)
    descricao = models.TextField()
    valor_estimado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    data_fechamento = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.descricao}'
    
    
    class Meta:
        db_table = "Oportunidade"

