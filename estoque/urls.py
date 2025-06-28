from django.urls import path
from . import views

app_name = 'estoque'

urlpatterns = [
    path('', views.home, name='home'),
    path('materiais/', views.lista_materiais, name='lista_materiais'),
    path('materiais/<int:pk>/', views.detalhe_material, name='detalhe_material'),
    path('movimentacoes/', views.lista_movimentacoes, name='lista_movimentacoes'),
]