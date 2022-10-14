# Create your models here.

from django.db import models
from datetime import date

#
class Reservas(models.Model):  
  id = models.IntegerField(primary_key=True, verbose_name="ID de Reserva")
  fecha_reserva = models.DateField(auto_now_add=False, auto_now=False , blank=False, verbose_name="Fecha de reserva (dd/mm/yyyy)", null=True)  
  nro_habitacion = models.IntegerField(verbose_name="Número de habitación", default=0)
  
  rut_huesped = models.ForeignKey("Huespedes", on_delete=models.CASCADE, blank=True , null=True)
  
  timestamp = models.DateField(auto_now_add=True, auto_now=False , blank=True, verbose_name="", null=True)
  
  #
  # def __str__(self):
  #   return self.


#
class Huespedes(models.Model):
  #
  select_sexo = (
    ('M', "Masculino"),
    ('F', "Femenino")
  )
  
  #  
  rut = models.CharField(primary_key=True, max_length=13, verbose_name="Rut Huesped")
  nombre_completo = models.CharField(max_length=50, verbose_name="Nombre Completo", null=True)  
  sexo = models.CharField(max_length=1, verbose_name="Sexo", null=True, choices=select_sexo, default='')
  fecha_nacimiento = models.DateField(auto_now_add=False, auto_now=False , blank=False, verbose_name="Fecha de nacimiento (dd/mm/yyyy)", null=True)    
  telefono_contacto = models.CharField(max_length=15, verbose_name="Teléfono", null=True)
        
  #
  def __str__(self):
    return self.nombre_completo


#
class Usuarios(models.Model):  
  nombre_usuario = models.CharField(primary_key=True, max_length=20, verbose_name="Nombre Usuario")
  contrasenna = models.CharField(max_length=20, verbose_name="Contraseña")
  correo_electronico = models.CharField(max_length=20, verbose_name="Correo Electrónico")  
  
  #
  def __str__(self):
    return self.nombre_usuario
  
  

  