__author__ = 'developer'
# -*- encoding: utf-8 -*-
from django.forms.widgets import *
from django import forms
from principal.models import Agenda, Direcciones


class CrearContactoForm(forms.ModelForm):

	class Meta:
		model = Agenda
		widgets = {
			'nombre': TextInput(attrs={'class': 'form-control required', 'placeholder': 'Fulanito'}),
			'apellidos': TextInput(attrs={'class': 'form-control required', 'placeholder': 'Perez Perez'}),
			'telefono': TextInput(attrs={'class': 'form-control required', 'placeholder': '55-55-55-55-55'}),
			'correo': EmailInput(attrs={'class': 'form-control required', 'placeholder': 'fulanito@hotmail.com'}),
			'redes_sociales': Select(attrs={'class': 'form-control required'}),
		}
		exclude = ['fecha_registro', 'cat_estatus']


class EditarContactoForm(forms.ModelForm):

	class Meta:
		model = Agenda
		widgets = {
			'nombre': TextInput(attrs={'class': 'form-control required', 'placeholder': 'Fulanito'}),
			'apellidos': TextInput(attrs={'class': 'form-control required', 'placeholder': 'Perez Perez'}),
			'telefono': TextInput(attrs={'class': 'form-control required', 'placeholder': '55-55-55-55-55'}),
			'correo': EmailInput(attrs={'class': 'form-control required', 'placeholder': 'fulanito@hotmail.com'}),
			'redes_sociales': Select(attrs={'class': 'form-control required'}),
		}
		exclude = ['fecha_registro', 'cat_estatus']


class EliminarContactoForm(forms.ModelForm):

	class Meta:
		model = Agenda
		widgets = {
			'nombre': TextInput(attrs={'class': 'form-control required', 'placeholder': 'Fulanito'}),
			'apellidos': TextInput(attrs={'class': 'form-control required', 'placeholder': 'Perez Perez'}),
			'telefono': TextInput(attrs={'class': 'form-control required', 'placeholder': '55-55-55-55-55'}),
			'correo': EmailInput(attrs={'class': 'form-control required', 'placeholder': 'fulanito@hotmail.com'}),
			'redes_sociales': Select(attrs={'class': 'form-control required'}),
		}
		exclude = ['fecha_registro', 'cat_estatus']


class CrearDireccionContactoForm(forms.ModelForm):
	class Meta:
		model = Direcciones
		widgets = {
		'nombre': TextInput(attrs={'class': 'form-control required', 'placeholder': 'Fracc. San Angel'}),
		'ciudad': TextInput(attrs={'class': 'form-control required', 'placeholder': 'Villahermosa, Tabasco'}),
		'calle': TextInput(attrs={'class': 'form-control required', 'placeholder': 'El Aguila'}),
		'codigo_postal': TextInput(attrs={'class': 'form-control required', 'placeholder': '80100'}),
		'tipo_direccion': Select(attrs={'class': 'form-control required'}),
		}
		fields = ['tipo_direccion', 'nombre', 'ciudad', 'calle', 'codigo_postal']
		exclude = ['fecha_registro', 'cat_estatus', 'agenda']


class EditarDireccionContactoForm(forms.ModelForm):
	class Meta:
		model = Direcciones
		widgets = {
		'nombre': TextInput(attrs={'class': 'form-control required', 'placeholder': 'Fracc. San Angel'}),
		'ciudad': TextInput(attrs={'class': 'form-control required', 'placeholder': 'Villahermosa, Tabasco'}),
		'calle': TextInput(attrs={'class': 'form-control required', 'placeholder': 'El Aguila'}),
		'codigo_postal': TextInput(attrs={'class': 'form-control required', 'placeholder': '80100'}),
		'tipo_direccion': Select(attrs={'class': 'form-control required'}),
		}
		fields = ['tipo_direccion', 'nombre', 'ciudad', 'calle', 'codigo_postal']
		exclude = ['fecha_registro', 'cat_estatus', 'agenda']
