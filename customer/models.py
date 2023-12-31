from django.db import models
from django.urls import reverse
from django.utils import timezone


class Customer(models.Model):
    first_name = models.CharField( max_length=30)
    last_name = models.CharField( max_length=50)
    email = models.EmailField()
    bird_date = models.DateField()
    area_code = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=9)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_full_phone_number(self):
        return f'({self.area_code}) {self.phone_number}'
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_full_city(self):
        return f'{self.city} - {self.state}'
    
    def get_absolute_url(self):
        return reverse("customer:update", kwargs={"id": self.id})
    
    def get_delete_url(self):
        return reverse("customer:delete", kwargs={"id": self.id})
    
    class Meta:
        db_table = "customer"


class Contato (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    create_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    cliente = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return f' {self.first_name}'
    
    def get_full_contato(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        db_table = "contato"