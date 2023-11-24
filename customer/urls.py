

from django.urls import path
from .views import ListCustomer, CreateCustomer, UpdateCustomer, DeleteCustomer


app_name = "customer"

urlpatterns = [

    path('list/', ListCustomer.as_view(), name='list'),
    path('create/', CreateCustomer.as_view(), name='create'),
    path('<int:id>/', UpdateCustomer.as_view(), name='update'),
    path('<int:id>/delete/', DeleteCustomer.as_view(), name='delete'),
]
