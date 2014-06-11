# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WaterT'
        db.create_table(u'balmy_beach_watert', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('surf_temp', self.gf('django.db.models.fields.IntegerField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'balmy_beach', ['WaterT'])

        # Adding model 'AirT'
        db.create_table(u'balmy_beach_airt', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('air_temp', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'balmy_beach', ['AirT'])

        # Adding model 'WaterQuality'
        db.create_table(u'balmy_beach_waterquality', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ecoli', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'balmy_beach', ['WaterQuality'])


    def backwards(self, orm):
        # Deleting model 'WaterT'
        db.delete_table(u'balmy_beach_watert')

        # Deleting model 'AirT'
        db.delete_table(u'balmy_beach_airt')

        # Deleting model 'WaterQuality'
        db.delete_table(u'balmy_beach_waterquality')


    models = {
        u'balmy_beach.airt': {
            'Meta': {'object_name': 'AirT'},
            'air_temp': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'balmy_beach.waterquality': {
            'Meta': {'object_name': 'WaterQuality'},
            'ecoli': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'balmy_beach.watert': {
            'Meta': {'object_name': 'WaterT'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'surf_temp': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['balmy_beach']