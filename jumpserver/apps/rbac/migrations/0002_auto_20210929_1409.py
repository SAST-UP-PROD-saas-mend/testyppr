# Generated by Django 3.1.13 on 2021-11-30 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='permission',
            options={'verbose_name': 'Permissions'},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'verbose_name': 'Role'},
        )
    ]
