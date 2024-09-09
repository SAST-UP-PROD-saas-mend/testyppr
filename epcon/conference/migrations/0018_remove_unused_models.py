# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-01-15 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0017_retire_more_unused_models'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deadlinecontent',
            name='deadline',
        ),
        migrations.AlterUniqueTogether(
            name='eventbooking',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='eventbooking',
            name='event',
        ),
        migrations.RemoveField(
            model_name='eventbooking',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='eventinterest',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='eventinterest',
            name='event',
        ),
        migrations.RemoveField(
            model_name='eventinterest',
            name='user',
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
        migrations.DeleteModel(
            name='Deadline',
        ),
        migrations.DeleteModel(
            name='DeadlineContent',
        ),
        migrations.DeleteModel(
            name='EventBooking',
        ),
        migrations.DeleteModel(
            name='EventInterest',
        ),
    ]
