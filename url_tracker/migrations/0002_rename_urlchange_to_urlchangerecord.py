# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_table('url_tracker_urlchange', 'url_tracker_urlchangerecord')


    def backwards(self, orm):
        db.rename_table('url_tracker_urlchangerecord', 'url_tracker_urlchange')


    models = {
        'url_tracker.urlchangerecord': {
            'Meta': {'object_name': 'URLChangeRecord'},
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new_url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'old_url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['url_tracker']
