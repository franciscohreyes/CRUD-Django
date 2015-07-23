# encoding:utf-8
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from requests import request
from catalogos.forms import CrearEstatusForm, EditarEstatusForm
from catalogos.models import Cat_estatus


class ListaEstatusView(ListView):
	model = Cat_estatus
	template_name = "cat_estatus_list.html"
	queryset = Cat_estatus.objects.all().order_by('id')

	def get_filter(self, queryset):
		search = self.get_search()
		if search:
			queryset = queryset.filter(
				Q(nombre__icontains=search)
			)
		return queryset

	def get_context_data(self, **kwargs):
		context = super(ListaEstatusView, self).get_context_data(**kwargs)
		context['estatus'] = 'open'
		return context


class AgregarEstatusView(CreateView):
	model = Cat_estatus
	form_class = CrearEstatusForm
	success_url = reverse_lazy("lista_estatus")
	template_name = "cat_estatus_form.html"

	def form_valid(self, form):
		datos = form.cleaned_data["descripcion"]
		estatus = Cat_estatus.objects.filter(descripcion=datos)
		if estatus:
			messages.error(self.request, "Ya existe un estatus con el nombre de: " + datos)
			return HttpResponseRedirect(reverse_lazy('agregar_nuevo_estatus'))
		messages.success(self.request, "Se agrego un estatus correctamente")
		return super(AgregarEstatusView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(AgregarEstatusView, self).get_context_data(**kwargs)
		context['estatus'] = 'open'
		return context


class DetalleEstatusView(DetailView):
	model = Cat_estatus
	template_name = "cat_estatus_detail.html"

	def get_context_data(self, **kwargs):
		context = super(DetalleEstatusView, self).get_context_data(**kwargs)
		context['estatus'] = 'open'
		return context


class EditarEstatusView(UpdateView):
	model = Cat_estatus
	form_class = EditarEstatusForm
	success_url = reverse_lazy("lista_estatus")
	template_name = "cat_estatus_update_form.html"

	def form_valid(self, form):
		messages.success(self.request, "Se actualizó el estatus correctamente")
		return super(EditarEstatusView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(EditarEstatusView, self).get_context_data(**kwargs)
		context['estatus'] = 'open'
		return context
