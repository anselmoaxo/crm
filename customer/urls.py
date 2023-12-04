

from django.urls import path
from .views import ListCustomer, CreateCustomer, UpdateCustomer, DeleteCustomer, ListContato, CreateContato, DeleteContato, UpdateContato


app_name = "customer"

urlpatterns = [

    path('list/', ListCustomer.as_view(), name='list'),
    path('create/', CreateCustomer.as_view(), name='create'),
    path('<int:id>/', UpdateCustomer.as_view(), name='update'),
    path('<int:id>/delete/', DeleteCustomer.as_view(), name='delete'),

    path('contato_list/', ListContato.as_view(), name='contato_list'),
    path('contato_create/', CreateContato.as_view(), name='contato_create'),
    path('contato/<int:id>/', UpdateContato.as_view(), name='contato_update'),
    path('contato/<int:id>/delete/', DeleteContato.as_view(), name='contato_delete'),
    
]
