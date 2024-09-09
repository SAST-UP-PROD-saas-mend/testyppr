# Generated by Django 4.1.6 on 2023-03-01 21:08

import django.db.models.deletion
from django.db import migrations, models

import peeringdb.models


class Migration(migrations.Migration):
    dependencies = [("peeringdb", "0025_carrier_objects_sync_rename")]

    operations = [
        migrations.CreateModel(
            name="Campus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("name_long", models.CharField(blank=True, max_length=255, null=True)),
                ("aka", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "website",
                    peeringdb.models.URLField(blank=True, max_length=255, null=True),
                ),
                ("notes", models.TextField(blank=True)),
                (
                    "org",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="campus_set",
                        to="peeringdb.organization",
                        verbose_name="Organization",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "campuses",
            },
        ),
        migrations.AddField(
            model_name="carrierfacility",
            name="campus",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="carrierfac_set",
                to="peeringdb.campus",
                verbose_name="Campus",
            ),
        ),
        migrations.AddField(
            model_name="facility",
            name="campus",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="fac_set",
                to="peeringdb.campus",
                verbose_name="Campus",
            ),
        ),
    ]
