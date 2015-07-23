__author__ = 'developer'
# -*- encoding: utf-8 -*-
from django.forms.widgets import *
from django import forms
from principal.models import Agenda


class CrearContactoForm(forms.ModelForm):

	class Meta:
		model = Agenda
		widgets = {
			'nombre': TextInput(attrs={'class': 'form-control', 'placeholder': 'Fulanito'}),
			'apellidos': TextInput(attrs={'class': 'form-control required', 'placeholder': 'Perez Perez'}),
			'direccion': Textarea(attrs={'class': 'form-control required', 'placeholder': 'Col. Centro'}),
			'telefono': NumberInput(attrs={'class': 'form-control required', 'placeholder': '55-55-55-55-55'}),
			'correo': EmailInput(attrs={'class': 'form-control required', 'placeholder': 'fulanito@hotmail.com'}),
			'redes_sociales': Select(attrs={'class': 'form-control required'}),
		}
		exclude = ['fecha_registro', 'cat_estatus']


class EditarContactoForm(forms.ModelForm):

	class Meta:
		model = Agenda
		widgets = {
			'nombre': TextInput(attrs={'class': 'form-control', 'placeholder': 'Fulanito'}),
			'apellidos': TextInput(attrs={'class': 'form-control required', 'placeholder': 'Perez Perez'}),
			'direccion': Textarea(attrs={'class': 'form-control required', 'placeholder': 'Col. Centro'}),
			'telefono': NumberInput(attrs={'class': 'form-control required', 'placeholder': '55-55-55-55-55'}),
			'correo': EmailInput(attrs={'class': 'form-control required', 'placeholder': 'fulanito@hotmail.com'}),
			'redes_sociales': Select(attrs={'class': 'form-control required'}),
		}
		exclude = ['fecha_registro', 'cat_estatus']


class EliminarContactoForm(forms.ModelForm):

	class Meta:
		model = Agenda
		exclude = ['fecha_registro', 'cat_estatus']
