

from django.urls import path
from .views import ListCustomer


app_name = "customer"

urlpatterns = [
    path('list/', ListCustomer.as_view(), name='list')
]
