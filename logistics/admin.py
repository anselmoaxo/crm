from django.contrib import admin
from .models import Produto, UnidadeMedida, EntradaNfe, SaidaNfe, Movimentacao

admin.site.register(Produto)
admin.site.register(UnidadeMedida)
admin.site.register(EntradaNfe)
admin.site.register(SaidaNfe)
admin.site.register(Movimentacao)