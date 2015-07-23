# encoding:utf-8
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.db import transaction
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from principal.forms import CrearContactoForm, EditarContactoForm, EliminarContactoForm
from principal.models import Agenda


class Inicio(TemplateView):
	template_name = "index.html"


class ListaContactosView(ListView):
	model = Agenda
	template_name = "list_agenda.html"
	queryset = Agenda.objects.filter(cat_estatus__descripcion="ACTIVO").order_by('id')

	def get_filter(self, queryset):
		search = self.get_search()
		if search:
			queryset = queryset.filter(
				Q(nombre__icontains=search)
			)
		return queryset

	def get_context_data(self, **kwargs):
		context = super(ListaContactosView, self).get_context_data(**kwargs)
		context['contacto'] = 'Active'
		return context


class ListaContactosInactivosView(ListView):
	model = Agenda
	template_name = "list_agenda_contactos_inactivos.html"
	queryset = Agenda.objects.filter(cat_estatus__descripcion="INACTIVO").order_by('id')

	def get_filter(self, queryset):
		search = self.get_search()
		if search:
			queryset = queryset.filter(
				Q(nombre__icontains=search)
			)
		return queryset

	def get_context_data(self, **kwargs):
		context = super(ListaContactosInactivosView, self).get_context_data(**kwargs)
		context['contacto'] = 'Active'
		return context


class AgregarContactoView(CreateView):
	model = Agenda
	form_class = CrearContactoForm
	success_url = reverse_lazy("lista_contactos_nuevos")
	template_name = "agenda_form.html"

	@transaction.atomic()
	def form_valid(self, form):
		form.instance.cat_estatus_id = 1
		messages.success(self.request, "Se agrego correctamente un contacto")
		return super(AgregarContactoView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(AgregarContactoView, self).get_context_data(**kwargs)
		context['contacto'] = 'Active'
		return context


class DetalleContactoView(DetailView):
	model = Agenda
	template_name = "agenda_detail.html"

	def get_context_data(self, **kwargs):
		context = super(DetalleContactoView, self).get_context_data(**kwargs)
		context['contacto'] = 'Active'
		return context


class EditarContactoView(UpdateView):
	model = Agenda
	form_class = EditarContactoForm
	success_url = reverse_lazy("lista_contactos_nuevos")
	template_name = "agenda_update_form.html"

	def form_valid(self, form):
		form.instance.cat_estatus_id = 1
		return super(EditarContactoView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(EditarContactoView, self).get_context_data(**kwargs)
		context['contacto'] = 'Active'
		return context


class EliminarContactoView(UpdateView):
	model = Agenda
	form_class = EliminarContactoForm
	success_url = reverse_lazy("lista_contactos_nuevos")
	template_name = "agenda_confirm_delete.html"

	def form_valid(self, form):
		form.instance.cat_estatus_id = 2
		return super(EliminarContactoView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(EliminarContactoView, self).get_context_data(**kwargs)
		context['contacto'] = 'Active'
		return context