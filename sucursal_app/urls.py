from django.urls import path
from sucursal_app import views

urlpatterns = [
    path("sucursales", views.inicio_vistaSucursales, name="sucursales"),
    path("registrarSucursal/", views.registrarSucursal, name="registrarSucursal"),
    path("seleccionarSucursal/<codigo>", views.seleccionarSucursal, name="seleccionarSucursal"),
    path("editarSucursal/", views.editarSucursal, name="editarSucursal"),
    path("borrarSucursal/<codigo>", views.borrarSucursal, name="borrarSucursal"),
]
