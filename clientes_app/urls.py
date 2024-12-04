from django.urls import path
from clientes_app import views

urlpatterns = [
    path("clientes", views.gestionar_clientes, name="clientes"),
    path("registrarCliente/", views.registrar_cliente, name="registrar_cliente"),
    path("seleccionarCliente/<int:id_cliente>/", views.seleccionar_cliente, name="seleccionar_cliente"),
    path("editarCliente/", views.editar_cliente, name="editar_cliente"),
    path("borrarCliente/<int:id_cliente>/", views.borrar_cliente, name="borrar_cliente"),
]
