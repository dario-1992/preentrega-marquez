from Registro import views
from django.urls import path



urlpatterns = [
    path('Inicio/', views.Inicio, name = "inicio"),
    path('Clientes/', views.Cliente, name = "cliente" ),
    path('Productos/', views.Producto, name = "producto"),
    path('Entregas/', views.Entrega, name = "entrega"),
    path('cliente-formulario/', views.cliente_formulario, name = "clienteFormulario"),
]
