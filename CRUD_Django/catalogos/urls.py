# encoding:utf-8
from django.conf.urls import include, url
from django.contrib import admin
from catalogos.views import ListaEstatusView, AgregarEstatusView, DetalleEstatusView, EditarEstatusView

urlpatterns = [

    url(r'^ListaEstatus/$', ListaEstatusView.as_view(), name='lista_estatus'),
    url(r'^AgregarEstatus/$', AgregarEstatusView.as_view(), name='agregar_nuevo_estatus'),
    url(r'^DetalleEstatus/(?P<pk>\d+)/detalle/$', DetalleEstatusView.as_view(), name='detalle_nuevo_estatus'),
    url(r'^EditarEstatus/(?P<pk>\d+)/editar/$', EditarEstatusView.as_view(), name='editar_nuevo_estatus'),
]
