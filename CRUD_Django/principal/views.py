# encoding:utf-8
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy, reverse
from django.db import transaction
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from principal.forms import CrearContactoForm, EditarContactoForm, EliminarContactoForm, CrearDireccionContactoForm, EditarDireccionContactoForm
from principal.models import Agenda, Direcciones
from catalogos.models import Cat_estatus


class Inicio(TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super(Inicio, self).get_context_data(**kwargs)
		contactos_registrados = Agenda.objects.filter(cat_estatus__descripcion="ACTIVO").count()
		contactos_eliminados = Agenda.objects.filter(cat_estatus__descripcion="INACTIVO").count()
		direcciones_registradas = Direcciones.objects.filter(cat_estatus__descripcion="ACTIVO").count()
		estatus_registrados = Cat_estatus.objects.all().count()
		context['contactos_registrados'] = contactos_registrados
		context['contactos_eliminados'] = contactos_eliminados
		context['direcciones_registradas'] = direcciones_registradas
		context['estatus_registrados'] = estatus_registrados
		return context


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
		context['contacto'] = 'open'
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
		context['contacto'] = 'open'
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
		context['contacto'] = 'open'
		return context


class DetalleContactoView(DetailView):
	model = Agenda
	template_name = "agenda_detail.html"

	def get_context_data(self, **kwargs):
		context = super(DetalleContactoView, self).get_context_data(**kwargs)
		direcciones = Direcciones.objects.filter(agenda_id=self.kwargs["pk"], cat_estatus__descripcion="ACTIVO").order_by('id')
		context['contacto'] = 'open'
		context['direcciones'] = direcciones
		return context


class EditarContactoView(UpdateView):
	model = Agenda
	form_class = EditarContactoForm
	success_url = reverse_lazy("lista_contactos_nuevos")
	template_name = "agenda_update_form.html"

	def form_valid(self, form):
		form.instance.cat_estatus_id = 1
		messages.success(self.request, "Se actualizó correctamente el contacto")
		return super(EditarContactoView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(EditarContactoView, self).get_context_data(**kwargs)
		context['contacto'] = 'open'
		context['editar'] = 'editar'
		return context


class ActivarContactoView(UpdateView):
	model = Agenda
	form_class = EditarContactoForm
	success_url = reverse_lazy("lista_contactos_inactivos")
	template_name = "agenda_update_form.html"

	def form_valid(self, form):
		form.instance.cat_estatus_id = 1
		messages.success(self.request, "Se activó correctamente el contacto")
		return super(ActivarContactoView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(ActivarContactoView, self).get_context_data(**kwargs)
		context['contacto'] = 'open'
		context['activar'] = 'activar'
		return context


class EliminarContactoView(UpdateView):
	model = Agenda
	form_class = EliminarContactoForm
	success_url = reverse_lazy("lista_contactos_nuevos")
	template_name = "agenda_confirm_delete.html"

	def form_valid(self, form):
		form.instance.cat_estatus_id = 2
		messages.success(self.request, "Se eliminó correctamente el contacto")
		return super(EliminarContactoView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(EliminarContactoView, self).get_context_data(**kwargs)
		context['contacto'] = 'open'
		context['eliminar'] = 'eliminar'
		return context


class ListaDireccionesView(ListView):
	model = Direcciones
	template_name = "list_direcciones.html"
	queryset = Direcciones.objects.filter(cat_estatus__descripcion="ACTIVO").order_by('id')

	def get_filter(self, queryset):
		search = self.get_search()
		if search:
			queryset = queryset.filter(
				Q(nombre__icontains=search)
			)
		return queryset

	def get_context_data(self, **kwargs):
		context = super(ListaDireccionesView, self).get_context_data(**kwargs)
		context['contacto'] = 'open'
		return context


class AgregarDireccionContactoView(CreateView):
	model = Direcciones
	form_class = CrearDireccionContactoForm
	template_name = "direccion_form.html"

	def get_success_url(self):
		contacto = Agenda.objects.get(pk=self.kwargs["pk"])
		return reverse('detalle_contacto_nuevo', kwargs={'pk': contacto.id})

	@transaction.atomic()
	def form_valid(self, form):
		form.instance.cat_estatus_id = 1
		form.instance.agenda_id = self.kwargs["pk"]
		messages.success(self.request, "Se agrego correctamente una dirección al contacto")
		return super(AgregarDireccionContactoView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(AgregarDireccionContactoView, self).get_context_data(**kwargs)
		context['contacto'] = 'open'
		return context


class EditarDireccionContactoView(UpdateView):
	model = Direcciones
	form_class = EditarDireccionContactoForm
	success_url = reverse_lazy("lista_contactos_nuevos")
	template_name = "direccion_update_form.html"

	@transaction.atomic()
	def form_valid(self, form):
		form.instance.cat_estatus_id = 1
		messages.success(self.request, "Se actualizó correctamente la direccion del contacto")
		return super(EditarDireccionContactoView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(EditarDireccionContactoView, self).get_context_data(**kwargs)
		context['contacto'] = 'open'
		return context


class EliminarDireccionContactoView(UpdateView):
	model = Direcciones
	form_class = EditarDireccionContactoForm
	success_url = reverse_lazy("lista_contactos_nuevos")
	template_name = "direccion_update_form.html"

	@transaction.atomic()
	def form_valid(self, form):
		form.instance.cat_estatus_id = 2
		messages.success(self.request, "Se eliminó correctamente la direccion del contacto")
		return super(EliminarDireccionContactoView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(EliminarDireccionContactoView, self).get_context_data(**kwargs)
		context['contacto'] = 'open'
		context['eliminar'] = 'eliminar'
		return context