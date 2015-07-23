# encoding:utf-8
from django.db import models

class Cat_estatus(models.Model):
	descripcion = models.CharField(max_length=50)

	def __str__(self):
		return '%s' % self.descripcion
