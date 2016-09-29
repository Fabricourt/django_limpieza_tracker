from __future__ import unicode_literals

from django.db import models

# Create your models here.

class opeDuquesa(models.Model):
	id = models.AutoField(primary_key=True)
	date = models.DateField()
	ficha_camion = models.CharField(max_length=15)
	circunscripcion = models.CharField(max_length=2)
	ton = models.IntegerField()

def __unicode__(self):
		return u'%s' % (self.date) 