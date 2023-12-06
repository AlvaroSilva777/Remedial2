from django.db import models
class Propietario(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre

class Estadio(models.Model):
    nombre = models.CharField(max_length=255)
    capacidad = models.IntegerField()
    tamaño = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    nombre = models.CharField(max_length=255)
    posicion = models.CharField(max_length=255)
    numero = models.IntegerField()
    equipo = models.ForeignKey('Equipo', on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=255)
    Propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    estadio = models.ForeignKey(Estadio, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Evento(models.Model):
    nombre = models.CharField(max_length=255)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
