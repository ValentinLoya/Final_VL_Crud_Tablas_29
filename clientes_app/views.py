from django.shortcuts import render, redirect
from .models import Cliente

def gestionar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "gestionarCliente.html", {"clientes": clientes})

def registrar_cliente(request):
    
    Cliente.objects.create(
        id_cliente=request.POST["id_cliente"],
        nombre=request.POST["nombre"],
        id_venta=request.POST["id_venta"],
        edad=request.POST["edad"],
        sexo=request.POST["sexo"],
        correo_electronico=request.POST["correo_electronico"],
        presupuesto=request.POST["presupuesto"],
        id_sucursal=request.POST["id_sucursal"],
    )
    return redirect("clientes")

def seleccionar_cliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    return render(request, "editarCliente.html", {"cliente": cliente})

def editar_cliente(request):
    id_cliente=request.POST["id_cliente"]
    nombre= request.POST["nombre"]
    id_venta = request.POST["id_venta"]
    edad = request.POST["edad"]
    sexo = request.POST["sexo"]
    correo_electronico = request.POST["correo_electronico"]
    presupuesto = request.POST["presupuesto"]
    id_sucursal = request.POST["id_sucursal"]

    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.nombre = nombre
    cliente.id_venta = id_venta
    cliente.edad = edad
    cliente.sexo = sexo
    cliente.correo_electronico = correo_electronico
    cliente.presupuesto = presupuesto
    cliente.id_sucursal = id_sucursal
    cliente.save()
    return redirect("clientes")

def borrar_cliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect("clientes")
