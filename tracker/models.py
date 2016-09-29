from __future__ import unicode_literals

from django.db import models

# Create your models here.

class opeduquesa(models.Model):
	date = models.Datefield()
	ficha_camion = models.CharField()
	circunscripcion = models.CharField(max_length=2)
	ton = models.IntegerField(max_length=10)
	
