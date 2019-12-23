from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Supervisor(models.Model):
	nombre = models.CharField(max_length=50, unique=True, primary_key=True)
	flota = models.CharField(max_length=14)
	telefono = models.CharField(max_length=14)
	compactadores = models.IntegerField()
	camioncitos = models.IntegerField()

	def __unicode__(self):
		return u'%s' % (self.nombre)



class Sectores(models.Model):
	nombre = models.CharField(max_length=30, unique=True, primary_key=True)
	supervisor_area = models.ForeignKey(Supervisor)

	def __unicode__(self):
		return u'%s' % (self.nombre)



class Circunscripcion(models.Model):
	num = models.CharField(max_length=6, unique=True, primary_key=True)
	sectores = models.ManyToManyField(Sectores)
	capacidad = models.FloatField()

	def __unicode__(self):
		return u'%s' % (self.num)


class Camion(models.Model):
	ficha = models.CharField(max_length=20, unique=True, primary_key=True)
	tipo_camion = models.CharField(max_length=20)
	capacidad = models.IntegerField()

	def __unicode__(self):
		return u'%s' % (self.ficha)


class SalidaTransfer(models.Model):
	camion = models.ForeignKey(Camion)
	ton = models.FloatField()


class Transfer(models.Model):
	camion = models.ForeignKey(Camion)
	viaje = models.IntegerField()
	ton_aproximado = models.IntegerField()

	def __unicode__(self):
		return u'%s' % (self.camion)


class TransferComlursa(models.Model):
	camion = models.ForeignKey(Camion)
	circunscripcion = models.ForeignKey(Circunscripcion)
	viaje = models.IntegerField()
	ton_aproximado = models.IntegerField()

	def __unicode__(self):
		return u'%s' % (self.camion)

class opeDuquesa(models.Model):
	id = models.AutoField(primary_key=True)
	date = models.DateField()
	camion = models.ForeignKey(Camion)
	circunscripcion = models.ForeignKey(Circunscripcion)
	ton = models.FloatField()
	viajes = models.IntegerField()

	def __unicode__(self):
		return u'%s' % (self.date)

class Compania(models.Model):
	nombre = models.CharField(max_length=20)
	camiones_owned = models.ManyToManyField(Camion)

	def __unicode__(self):
		return u'%s' % (self.nombre)








