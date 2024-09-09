# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-21 18:58
from __future__ import unicode_literals

from django.db import migrations, models


def change_boot_scrubs(apps, schema_editor):
    Advanced = apps.get_model('system', 'Advanced')
    queryset = Advanced.objects.filter(adv_boot_scrub=35)
    for query in queryset:
        query.adv_boot_scrub = 7
        query.save()


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0006_update_tun_var_size'),
    ]

    operations = [
        migrations.RunPython(change_boot_scrubs),
        migrations.AlterField(
            model_name='Advanced',
            name='adv_boot_scrub',
            field=models.IntegerField(editable=False, default=7),
        ),
    ]
