from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuarios(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	department = models.CharField(max_length=100)
	created = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return u'%s' % self.user
