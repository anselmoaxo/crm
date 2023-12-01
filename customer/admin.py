from django.contrib import admin
from .models import Customer, Contato


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')

