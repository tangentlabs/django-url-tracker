# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'URLChange'
        db.create_table('url_tracker_urlchange', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('old_url', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('new_url', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('url_tracker', ['URLChange'])


    def backwards(self, orm):
        
        # Deleting model 'URLChange'
        db.delete_table('url_tracker_urlchange')


    models = {
        'url_tracker.urlchange': {
            'Meta': {'object_name': 'URLChange'},
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new_url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'old_url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['url_tracker']
