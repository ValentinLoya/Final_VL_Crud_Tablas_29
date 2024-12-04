from django.db import models

# Create your models here.
class Producto(models.Model):
    id_producto=models.PositiveIntegerField(primary_key=True)
    id_sucursal=models.PositiveIntegerField()
    nombre=models.CharField(max_length=100)
    stock=models.PositiveIntegerField()
    id_provedor=models.PositiveIntegerField()
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    marca=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre