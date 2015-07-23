__author__ = 'developer'
# -*- encoding: utf-8 -*-
from django.forms.widgets import *
from django import forms
from catalogos.models import Cat_estatus


class CrearEstatusForm(forms.ModelForm):

	class Meta:
		model = Cat_estatus
		widgets = {
			'descripcion': TextInput(attrs={'class': 'form-control', 'placeholder': 'ACTIVO'}),
		}
		exclude = ['']


class EditarEstatusForm(forms.ModelForm):

	class Meta:
		model = Cat_estatus
		widgets = {
			'descripcion': TextInput(attrs={'class': 'form-control', 'placeholder': 'ACTIVO'}),
		}
		exclude = ['']
