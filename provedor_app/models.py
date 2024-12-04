from django.db import models

# Create your models here.
class Provedor(models.Model):
    id_provedor=models.PositiveIntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    empresa=models.CharField(max_length=50)
    num_celular=models.PositiveIntegerField()
    fecha_de_recorrido=models.DateField(null=False,blank=False)
    id_sucursal=models.PositiveIntegerField()

    def __str__(self):
        return self.id_provedor