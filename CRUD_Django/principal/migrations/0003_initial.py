# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Agenda'
        db.create_table('principal_agenda', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('apellidos', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('correo', self.gf('django.db.models.fields.EmailField')(max_length=100)),
            ('redes_sociales', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('fecha_registro', self.gf('django.db.models.fields.DateField')(blank=True, auto_now_add=True)),
            ('cat_estatus', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalogos.Cat_estatus'])),
        ))
        db.send_create_signal('principal', ['Agenda'])


    def backwards(self, orm):
        # Deleting model 'Agenda'
        db.delete_table('principal_agenda')


    models = {
        'catalogos.cat_estatus': {
            'Meta': {'object_name': 'Cat_estatus'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'principal.agenda': {
            'Meta': {'object_name': 'Agenda'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cat_estatus': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalogos.Cat_estatus']"}),
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fecha_registro': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'redes_sociales': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['principal']