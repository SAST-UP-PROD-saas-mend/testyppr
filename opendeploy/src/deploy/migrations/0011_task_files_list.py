# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-11 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0010_task_scope'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='files_list',
            field=models.TextField(default='', max_length=255, verbose_name='文件路径列表'),
        ),
    ]
