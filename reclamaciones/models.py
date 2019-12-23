from __future__ import unicode_literals

from django.db import models
from tracker.models import Sectores

# Create your models here.



class Reclamacion(models.Model):



	RECLAMACIONES_TYPES = (
        ('No pasa el camion','1-No pasa el camion'),
        ('Varios dias sin pasar','2-Varios dias sin pasar'),
        ('No pasa por la calle','3-No pasa por la calle'),
        ('Piden dinero','4-Piden dinero'),
        ('Escombros','5-Escombros'),
        ('Poda','6-Poda'),
        ('Camion no pasa el dia de su frecuencia','7-Camion no pasa el dia de su frecuencia'),
        ('Deficiencia servicio','8-Deficiencia servicio'),
        ('Camion pasa muy rapido','9-Camion pasa muy rapido'),
        ('No se detienen','10-No se detienen'),
        )


	fecha_apertura = models.DateField(blank=False)
	nombre = models.CharField(max_length=50, blank=False)
	direccion = models.CharField(max_length=200)
	sector = models.ForeignKey(Sectores, default='S/N')
	telefono = models.CharField(max_length=14)
	tipo_reclamacion = models.CharField(max_length=30, choices=RECLAMACIONES_TYPES)
	observaciones = models.TextField(max_length=300)
	fecha_cierre = models.DateField(null=True, blank=True)
	status = models.BooleanField(default=False)

        def __unicode__(self):
                return u'%s' % (self.nombre)









