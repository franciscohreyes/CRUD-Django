# encoding:utf-8
from django.db import models
from catalogos.models import Cat_estatus

REDES_SOCIALES = (
	('FB', 'Facebook'),
	('TW', 'Twitter'),
	('G+', 'Google Plus'),
	('Inst', 'Instagram')
)

class Agenda(models.Model):
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=100)
	direccion = models.CharField(max_length=100)
	telefono = models.CharField(max_length=100)
	correo = models.EmailField(max_length=100)
	redes_sociales = models.CharField(max_length=50, choices=REDES_SOCIALES)
	fecha_registro = models.DateField(auto_now_add=True)
	cat_estatus = models.ForeignKey(Cat_estatus)

	def __str__(self):
		return '%s - %s - %s' % (self.nombre, self.apellidos, self.cat_estatus.descripcion)