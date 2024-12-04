from django.shortcuts import render, redirect
from .models import Ventas

# Create your views here.
def inicio_vistaVentas(request):
    lasventas = Ventas.objects.all()
    return render(request, "gestionarVentas.html", {"misventas": lasventas})

def registrarVenta(request):
    id_venta = request.POST["txtcodigo"]
    id_cliente = request.POST["txtcliente"]
    id_empleado = request.POST["txtempleado"]
    hora_de_venta= request.POST["txttime"]
    total = request.POST["txttotal"]
    id_sucursal = request.POST["txtsucursal"]
    id_productos = request.POST["txtproducto"]
    fecha_venta = request.POST["txtfecha"]
    cantidad = request.POST["txtcantidad"]
    

    Ventas.objects.create(
        id_venta=id_venta,
        id_cliente=id_cliente,
        id_empleado=id_empleado,
        hora_de_venta=hora_de_venta,
        id_sucursal=id_sucursal,
        id_productos=id_productos,
        cantidad=cantidad,
        fecha_venta=fecha_venta,
        total=total,
    )  # GUARDA EL REGISTRO

    return redirect("ventas")

def seleccionarVenta(request, codigo):
    venta = Ventas.objects.get(id_venta=codigo)
    fecha_venta = venta.fecha_venta.strftime('%Y-%m-%d')
    hora_venta = venta.hora_de_venta.strftime('%H:%M:%S')
    return render(request, "editarVentas.html", {"misventas": venta, "misventas": venta, "fecha_venta": fecha_venta, "hora_venta" : hora_venta})

def editarVenta(request):
    id_venta = request.POST["txtcodigo"]
    id_cliente = request.POST["txtcliente"]
    id_empleado = request.POST["txtempleado"]
    hora_de_venta= request.POST["txttime"]
    total = request.POST["txttotal"]
    id_sucursal = request.POST["txtsucursal"]
    id_productos = request.POST["txtproducto"]
    fecha_venta = request.POST["txtfecha"]
    cantidad = request.POST["txtcantidad"]

    venta = Ventas.objects.get(id_venta=id_venta)
    venta.id_cliente = id_cliente
    venta.id_empleado = id_empleado
    venta.hora_de_venta = hora_de_venta
    venta.total = total
    venta.id_sucursal = id_sucursal
    venta.id_productos = id_productos
    venta.fecha_venta = fecha_venta
    venta.cantidad = cantidad
    
    venta.save()  # GUARDA EL REGISTRO ACTUALIZADO

    return redirect("ventas")

def borrarVenta(request, codigo):
    venta = Ventas.objects.get(id_venta=codigo)
    venta.delete()  # BORRA EL REGISTRO
    return redirect("ventas")
