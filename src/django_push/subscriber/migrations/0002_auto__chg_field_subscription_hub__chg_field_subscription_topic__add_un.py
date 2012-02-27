# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Subscription.hub'
        db.alter_column('subscriber_subscription', 'hub', self.gf('django.db.models.fields.URLField')(max_length=255))

        # Changing field 'Subscription.topic'
        db.alter_column('subscriber_subscription', 'topic', self.gf('django.db.models.fields.URLField')(max_length=255))

        # Adding unique constraint on 'Subscription', fields ['topic', 'hub']
        db.create_unique('subscriber_subscription', ['topic', 'hub'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Subscription', fields ['topic', 'hub']
        db.delete_unique('subscriber_subscription', ['topic', 'hub'])

        # Changing field 'Subscription.hub'
        db.alter_column('subscriber_subscription', 'hub', self.gf('django.db.models.fields.URLField')(max_length=1023))

        # Changing field 'Subscription.topic'
        db.alter_column('subscriber_subscription', 'topic', self.gf('django.db.models.fields.URLField')(max_length=1023))


    models = {
        'subscriber.subscription': {
            'Meta': {'unique_together': "(('hub', 'topic'),)", 'object_name': 'Subscription'},
            'hub': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lease_expiration': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'topic': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verify_token': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['subscriber']
