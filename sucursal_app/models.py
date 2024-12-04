from django.db import models

# Create your models here.
class Sucursal(models.Model):
    id_sucursal=models.PositiveIntegerField(primary_key=True)
    id_empleado=models.PositiveIntegerField()
    direccion=models.CharField(max_length=100)
    num_telefono=models.PositiveIntegerField()
    correo_electronico=models.EmailField(max_length=50)
    nombre=models.CharField(max_length=100)
    horario=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre