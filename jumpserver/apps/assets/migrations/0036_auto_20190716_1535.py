# Generated by Django 2.1.7 on 2019-07-16 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0035_auto_20190711_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commandfilter',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='Name'),
        ),
    ]
