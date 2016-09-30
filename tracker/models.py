from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Camion(models.Model):
	ficha = models.CharField(max_length=20, unique=True, primary_key=True)
	tipo_camion = models.CharField(max_length=20)
	capacidad = models.IntegerField()

	def __unicode__(self):
		return u'%s' % (self.ficha)

		
class opeDuquesa(models.Model):
	id = models.AutoField(primary_key=True)
	date = models.DateField()
	ficha_camion = models.ForeignKey(Camion)
	circunscripcion = models.CharField(max_length=2)
	ton = models.IntegerField()

	def __unicode__(self):
		return u'%s' % (self.date)

class Compania(models.Model):
	nombre = models.CharField(max_length=20)
	camiones = models.ManyToManyField(Camion)

	def __unicode__(self):
		return u'%s' % (self.nombre)







