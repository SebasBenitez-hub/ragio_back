from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Colab(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombreColab = models.CharField(max_length=100)
    tituloProf = models.CharField(max_length=100)
    correoColab = models.CharField(max_length=100)
    telefonoColab = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'

    def __str__(self):
        return self.nombreColab

class Cliente(models.Model):
    nombreFiscal = models.CharField(max_length=100)
    nombreComercial= models.CharField(max_length=100)
    poblacion = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    rfc = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nombreFiscal

class Servicio(models.Model):
    nombreServicio = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return self.nombreServicio

class Act(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    nombreActividad = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'

    def __str__(self):
        return  self.nombreActividad

class ActDiarias(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    colaborador = models.ForeignKey(Colab, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    actividad = models.ForeignKey(Act, on_delete=models.CASCADE)
    fecha = models.DateField()
    desdeHora = models.TimeField(auto_now=False)
    hastaHora = models.TimeField(auto_now=False)
    observacionAdicional = models.CharField(max_length=300, default='')
    porcentajeAvance = models.FloatField()

    class Meta:
        verbose_name = 'Actividad diaria'
        verbose_name_plural = 'Actividades diarias'

    def __str__(self):
        return '{} {} {}'.format(self.actividad, self.servicio, self.fecha)