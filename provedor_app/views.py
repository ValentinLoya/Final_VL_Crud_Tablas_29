from django.shortcuts import render, redirect
from .models import Provedor

def inicio_vistaProvedores(request):
    los_provedores = Provedor.objects.all()
    return render(request, "gestionarProvedor.html", {"mis_provedores": los_provedores})

def registrarProvedor(request):
    id_provedor = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    direccion = request.POST["txtdireccion"]
    empresa = request.POST["txtempresa"]
    num_celular = request.POST["txtcelular"]
    fecha_de_recorrido = request.POST["txtfecha"]
    id_sucursal = request.POST["txtsucursal"]

    Provedor.objects.create(
        id_provedor=id_provedor,
        nombre=nombre,
        direccion=direccion,
        empresa=empresa,
        num_celular=num_celular,
        fecha_de_recorrido=fecha_de_recorrido,
        id_sucursal=id_sucursal,
    )
    return redirect("provedores")

def seleccionarProvedor(request, codigo):
    provedor = Provedor.objects.get(id_provedor=codigo)
    fecha_de_recorrido=provedor.fecha_de_recorrido.strftime('%Y-%m-%d')
    return render(request,"editarProvedor.html",{"mi_provedor":provedor, "mi_provedor":provedor,"fecha_de_recorrido":fecha_de_recorrido})

def editarProvedor(request):
    id_provedor = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    direccion = request.POST["txtdireccion"]
    empresa = request.POST["txtempresa"]
    num_celular = request.POST["txtcelular"]
    fecha_de_recorrido = request.POST["txtfecha"]
    id_sucursal = request.POST["txtsucursal"]

    provedor = Provedor.objects.get(id_provedor=id_provedor)
    provedor.nombre = nombre
    provedor.direccion = direccion
    provedor.empresa = empresa
    provedor.num_celular = num_celular
    provedor.fecha_de_recorrido = fecha_de_recorrido
    provedor.id_sucursal = id_sucursal
    provedor.save()
    return redirect("provedores")

def borrarProvedor(request, codigo):
    provedor = Provedor.objects.get(id_provedor=codigo)
    provedor.delete()
    return redirect("provedores")
