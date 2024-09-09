# Generated by Django 2.0.3 on 2018-03-29 19:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("utils", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="useraction",
            name="action",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (1, "created"),
                    (2, "modified"),
                    (3, "deleted"),
                    (4, "imported"),
                    (5, "bulk deleted"),
                ]
            ),
        )
    ]
