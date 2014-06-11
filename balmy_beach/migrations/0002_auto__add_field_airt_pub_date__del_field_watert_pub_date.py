# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'AirT.pub_date'
        db.add_column(u'balmy_beach_airt', 'pub_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 6, 11, 0, 0)),
                      keep_default=False)

        # Deleting field 'WaterT.pub_date'
        db.delete_column(u'balmy_beach_watert', 'pub_date')


    def backwards(self, orm):
        # Deleting field 'AirT.pub_date'
        db.delete_column(u'balmy_beach_airt', 'pub_date')

        # Adding field 'WaterT.pub_date'
        db.add_column(u'balmy_beach_watert', 'pub_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 6, 11, 0, 0)),
                      keep_default=False)


    models = {
        u'balmy_beach.airt': {
            'Meta': {'object_name': 'AirT'},
            'air_temp': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 6, 11, 0, 0)'})
        },
        u'balmy_beach.waterquality': {
            'Meta': {'object_name': 'WaterQuality'},
            'ecoli': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'balmy_beach.watert': {
            'Meta': {'object_name': 'WaterT'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'surf_temp': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['balmy_beach']