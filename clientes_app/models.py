from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente=models.PositiveIntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    edad=models.PositiveIntegerField()
    sexo=models.CharField(max_length=50)
    correo_electronico=models.EmailField(max_length=50)
    presupuesto=models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.nombre