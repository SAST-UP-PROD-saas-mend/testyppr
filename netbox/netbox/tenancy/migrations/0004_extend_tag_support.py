# Generated by Django 3.2.8 on 2021-10-21 14:50

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0062_clear_secrets_changelog'),
        ('tenancy', '0003_contacts'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactgroup',
            name='tags',
            field=taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag'),
        ),
        migrations.AddField(
            model_name='contactrole',
            name='tags',
            field=taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag'),
        ),
        migrations.AddField(
            model_name='tenantgroup',
            name='tags',
            field=taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag'),
        ),
    ]
