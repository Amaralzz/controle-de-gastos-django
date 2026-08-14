from django.urls import path
from .views import listar_gastos, criar_gastos, editar_gasto, excluir_gasto, dashboard

urlpatterns = [
    path('', listar_gastos, name='listar_gastos'),
    path('criar/', criar_gastos, name='criar_gastos'),
    path('editar/<int:gasto_id>', editar_gasto, name = 'editar_gasto'),
    path('excluir/<int:gasto_id>', excluir_gasto, name='excluir_gasto'),
    path('dashboard/', dashboard, name='dashboard')
]