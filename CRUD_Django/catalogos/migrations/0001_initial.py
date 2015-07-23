# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cat_estatus'
        db.create_table('catalogos_cat_estatus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('catalogos', ['Cat_estatus'])


    def backwards(self, orm):
        # Deleting model 'Cat_estatus'
        db.delete_table('catalogos_cat_estatus')


    models = {
        'catalogos.cat_estatus': {
            'Meta': {'object_name': 'Cat_estatus'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['catalogos']