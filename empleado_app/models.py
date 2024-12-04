from django.db import models

# Create your models here.
class Empleado(models.Model):
    id_empleado=models.PositiveIntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    telefono=models.PositiveIntegerField()
    salario=models.DecimalField(max_digits=10, decimal_places=2)
    curp=models.CharField(max_length=50)
    edad=models.PositiveIntegerField()
    puesto=models.CharField(max_length=50)
    direccion=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre