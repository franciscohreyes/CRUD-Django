# encoding:utf-8
from django.conf.urls import include, url
from django.contrib import admin
from principal.views import Inicio, ListaContactosView, ListaContactosInactivosView, AgregarContactoView, DetalleContactoView, EditarContactoView, EliminarContactoView, AgregarDireccionContactoView, ListaDireccionesView, \
	EditarDireccionContactoView, ActivarContactoView, EliminarDireccionContactoView

urlpatterns = [

    url(r'^inicio/$', Inicio.as_view(), name='index'),
    url(r'^ListaContactos/$', ListaContactosView.as_view(), name='lista_contactos_nuevos'),
    url(r'^ContactosInactivos/$', ListaContactosInactivosView.as_view(), name='lista_contactos_inactivos'),
    url(r'^AgregarContacto/$', AgregarContactoView.as_view(), name='agregar_contacto_nuevo'),
    url(r'^DetalleContacto/(?P<pk>\d+)/detalle/$', DetalleContactoView.as_view(), name='detalle_contacto_nuevo'),
    url(r'^EditarContacto/(?P<pk>\d+)/editar/$', EditarContactoView.as_view(), name='editar_contacto_nuevo'),
    url(r'^ActivarContacto/(?P<pk>\d+)/activar/$', ActivarContactoView.as_view(), name='activar_contacto_nuevo'),
    url(r'^EliminarContacto/(?P<pk>\d+)/eliminar/$', EliminarContactoView.as_view(), name='eliminar_contacto_nuevo'),

    #URL's Direcciones de contacto
    url(r'^ListaDirecciones/$', ListaDireccionesView.as_view(), name='lista_direccion_contactos'),
    url(r'^DetalleContacto/(?P<pk>\d+)/agregardireccion/$', AgregarDireccionContactoView.as_view(), name='agregar_direccion_contacto'),
    url(r'^DetalleContacto/(?P<pk>\d+)/editardireccion/$', EditarDireccionContactoView.as_view(),
        name='editar_direccion_contacto'),
    url(r'^DetalleContacto/(?P<pk>\d+)/eliminardireccion/$', EliminarDireccionContactoView.as_view(),
        name='eliminar_direccion_contacto'),
]
