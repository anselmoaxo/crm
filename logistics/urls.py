from django.urls import path
from . import views




urlpatterns = [
    path('produto/', views.ProdutoCreate.as_view(), name="produto"),
    path('lista_prod/', views.ProdutoList.as_view(), name='lista_prod'),
    
    ]