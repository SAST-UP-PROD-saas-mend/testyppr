# Generated by Django 3.2.8 on 2021-10-09 16:23

from django.db import migrations

import peeringdb.models


class Migration(migrations.Migration):
    dependencies = [("peeringdb", "0019_auto_20210923_1544")]

    operations = [
        migrations.AlterField(
            model_name="facility",
            name="available_voltage_services",
            field=peeringdb.models.MultipleChoiceField(
                blank=True,
                choices=[
                    ("48 VDC", "48 VDC"),
                    ("120 VAC", "120 VAC"),
                    ("208 VAC", "208 VAC"),
                    ("240 VAC", "240 VAC"),
                    ("480 VAC", "480 VAC"),
                ],
                max_length=255,
                null=True,
            ),
        ),
    ]
