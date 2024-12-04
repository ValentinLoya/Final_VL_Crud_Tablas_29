from django.shortcuts import render, redirect
from .models import Empleado

def inicio_vistaEmpleados(request):
    los_empleados = Empleado.objects.all()
    return render(request, "gestionarEmpleado.html", {"mis_empleados": los_empleados})

def registrarEmpleado(request):
    id_empleado = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    salario = request.POST["txtsalario"]
    curp = request.POST["txtcurp"]
    edad = request.POST["txtedad"]
    puesto = request.POST["txtpuesto"]
    direccion = request.POST["txtdireccion"]

    Empleado.objects.create(
        id_empleado=id_empleado,
        nombre=nombre,
        telefono=telefono,
        salario=salario,
        curp=curp,
        edad=edad,
        puesto=puesto,
        direccion=direccion,
    )
    return redirect("empleados")

def seleccionarEmpleado(request, codigo):
    empleado = Empleado.objects.get(id_empleado=codigo)
    return render(request, "editarEmpleado.html", {"mi_empleado": empleado})

def editarEmpleado(request):
    id_empleado = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    salario = request.POST["txtsalario"]
    curp = request.POST["txtcurp"]
    edad = request.POST["txtedad"]
    puesto = request.POST["txtpuesto"]
    direccion = request.POST["txtdireccion"]

    empleado = Empleado.objects.get(id_empleado=id_empleado)
    empleado.nombre = nombre
    empleado.telefono = telefono
    empleado.salario = salario
    empleado.curp = curp
    empleado.edad = edad
    empleado.puesto = puesto
    empleado.direccion = direccion
    empleado.save()
    return redirect("empleados")

def borrarEmpleado(request, codigo):
    empleado = Empleado.objects.get(id_empleado=codigo)
    empleado.delete()
    return redirect("empleados")
