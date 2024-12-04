from django.urls import path
from provedor_app import views

urlpatterns = [
    path("provedores", views.inicio_vistaProvedores, name="provedores"),
    path("registrarProvedor/", views.registrarProvedor, name="registrarProvedor"),
    path("seleccionarProvedor/<codigo>", views.seleccionarProvedor, name="seleccionarProvedor"),
    path("editarProvedor/", views.editarProvedor, name="editarProvedor"),
    path("borrarProvedor/<codigo>", views.borrarProvedor, name="borrarProvedor"),
]
