from django.shortcuts import render, redirect
from .models import Producto

# Create your views here.
def inicio_vistaProducto(request):
    losproductos = Producto.objects.all()
    return render(request, "gestionarProducto.html", {"misproductos": losproductos})

def registrarProducto(request):
    id_producto = request.POST["txtcodigo"]
    id_sucursal = request.POST["txtsucursal"]
    nombre = request.POST["txtnombre"]
    stock = request.POST["txtstock"]
    id_provedor = request.POST["txtprovedor"]
    precio = request.POST["numprecio"]
    marca = request.POST["txtmarca"]

    Producto.objects.create(
        id_producto=id_producto,
        id_sucursal=id_sucursal,
        nombre=nombre,
        stock=stock,
        id_provedor=id_provedor,
        precio=precio,
        marca=marca,
    )

    return redirect("producto")

def seleccionarProducto(request, codigo):
    producto = Producto.objects.get(id_producto=codigo)
    return render(request, "editarproducto.html", {"misproductos": producto})

def editarProducto(request):
    id_producto = request.POST["txtcodigo"]
    id_sucursal = request.POST["txtsucursal"]
    nombre = request.POST["txtnombre"]
    stock = request.POST["txtstock"]
    id_provedor = request.POST["txtprovedor"]
    precio = request.POST["numprecio"]
    marca = request.POST["txtmarca"]

    producto = Producto.objects.get(id_producto=id_producto)
    producto.id_sucursal = id_sucursal
    producto.nombre = nombre
    producto.stock = stock
    producto.id_provedor = id_provedor
    producto.precio = precio
    producto.marca = marca

    producto.save()
    return redirect("producto")

def borrarProducto(request, codigo):
    producto = Producto.objects.get(id_producto=codigo)
    producto.delete()
    return redirect("producto")
