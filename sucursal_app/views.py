from django.shortcuts import render, redirect
from .models import Sucursal

def inicio_vistaSucursales(request):
    las_sucursales = Sucursal.objects.all()
    return render(request, "gestionarSucursales.html", {"mis_sucursales": las_sucursales})

def registrarSucursal(request):
    id_sucursal = request.POST["txtcodigo"]
    id_empleado = request.POST["txtidempleado"]
    direccion = request.POST["txtdireccion"]
    num_telefono = request.POST["numtelefono"]
    correo_electronico = request.POST["txtcorreo"]
    nombre = request.POST["txtnombre"]
    horario = request.POST["txthorario"]

    Sucursal.objects.create(
        id_sucursal=id_sucursal, id_empleado=id_empleado, direccion=direccion,
        num_telefono=num_telefono, correo_electronico=correo_electronico,
        nombre=nombre, horario=horario
    )
    return redirect("sucursales")

def seleccionarSucursal(request, codigo):
    sucursal = Sucursal.objects.get(id_sucursal=codigo)
    return render(request, "editarSucursal.html", {"mi_sucursal": sucursal})

def editarSucursal(request):
    id_sucursal = request.POST["txtcodigo"]
    id_empleado = request.POST["txtidempleado"]
    direccion = request.POST["txtdireccion"]
    num_telefono = request.POST["numtelefono"]
    correo_electronico = request.POST["txtcorreo"]
    nombre = request.POST["txtnombre"]
    horario = request.POST["txthorario"]

    sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursal.id_empleado = id_empleado
    sucursal.direccion = direccion
    sucursal.num_telefono = num_telefono
    sucursal.correo_electronico = correo_electronico
    sucursal.nombre = nombre
    sucursal.horario = horario
    sucursal.save()
    return redirect("sucursales")

def borrarSucursal(request, codigo):
    sucursal = Sucursal.objects.get(id_sucursal=codigo)
    sucursal.delete()
    return redirect("sucursales")
