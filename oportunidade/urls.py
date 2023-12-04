
from django.urls import path
from . import views

app_name = "oportunidade"

urlpatterns = [

    path('list/', views.OportunidadeList.as_view(), name='oportunidade_list'),
    path('create/', views.OportunidadeCreate.as_view(), name='oportunidade_create'),
]