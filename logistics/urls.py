from django.urls import path
from . import views


urlpatterns = [
    path('produto/', views.ProdutoCreate.as_view(), name="produto"),
    path('lista_prod/', views.ProdutoList.as_view(), name='lista_prod'),
    path('produto/<int:id>/', views.UpdateProduto.as_view(), name='produto_update'),
    path('produto/<int:id>/delete/', views.DeleteProduto.as_view(), name='produto_delete'),
    ]