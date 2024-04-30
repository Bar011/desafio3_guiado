from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    #Notas: el atributo de primary_key es para que el campo sea la clave primaria
    patente = models.CharField(max_length=6, primary_key=True)
    #Notas: el atributo de null es para que el campo sea nulo y el blank es para que no sea 'en blanco'.
    marca = models.CharField(max_length=20, null= False, blank= False)
    modelo = models.CharField(max_length=20, null= False, blank= False)
    year = models.IntegerField(null=False,blank=False)
    
class Chofer(models.Model):

    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null= False, blank= False)
    apellido = models.CharField(max_length=50, null= False, blank= False)
    activo = models.BooleanField(default=False)
    #nota: auto_now_add es para que se genere la fecha de creacion del registro
    #El auto_now es para que cada vez que se actualice el dato, se actualice la fecha de actualización
    creacion_registro = models.DateField(auto_now_add=True)
    #Notas: el atributo de related_name es para que el campo sea la clave primaria
    #Notas: on_delete = CASCADE es para que cuando se elimine un registro, se elimine el registro relacionado
    #Notas: on_delete = PROTECT es para que no se pueda eliminar el registro si tiene registros relacionados
    vehiculo =models.OneToOneField('Vehiculo', related_name='chofer',null=True,blank=True,on_delete=models.PROTECT)
    
class RegistroContabilidad(models.Model):
    #Django ya genera de por si la clave primaria, y siempre será de nombre 'ID'
    fecha_compra= models.DateField(null= False, blank= False)
    valor= models.FloatField(null= False, blank= False)
    vehiculo = models.OneToOneField('Vehiculo',related_name='contabilidad',on_delete=models.PROTECT)
    
