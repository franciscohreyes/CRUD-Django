from django.conf.urls import include, url
from django.contrib import admin
from principal.views import Inicio

urlpatterns = [

    url(r'^inicio/', Inicio.as_view(), name='inicio'),
]
