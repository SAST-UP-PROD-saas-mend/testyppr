# Generated by Django 2.1.4 on 2018-12-12 20:06

from django.db import migrations, models


class Migration(migrations.Migration):
    def forwards_func(apps, schema_editor):
        models = {
            "AutonomousSystem": {
                "filters": {"ipv4_max_prefixes": None, "ipv6_max_prefixes": None},
                "updates": {"ipv4_max_prefixes": 0, "ipv6_max_prefixes": 0},
            },
            "DirectPeeringSession": {
                "filters": {
                    "advertised_prefix_count": None,
                    "received_prefix_count": None,
                },
                "updates": {"advertised_prefix_count": 0, "received_prefix_count": 0},
            },
            "InternetExchange": {
                "filters": {"peeringdb_id": None},
                "updates": {"peeringdb_id": 0},
            },
            "InternetExchangePeeringSession": {
                "filters": {
                    "advertised_prefix_count": None,
                    "received_prefix_count": None,
                },
                "updates": {"advertised_prefix_count": 0, "received_prefix_count": 0},
            },
        }
        db_alias = schema_editor.connection.alias
        for key, value in models.items():
            model = apps.get_model("peering", key)
            model.objects.using(db_alias).filter(**value["filters"]).update(
                **value["updates"]
            )

    def reverse_func(apps, schema_editor):
        models = {
            "AutonomousSystem": {
                "filters": {"ipv4_max_prefixes": 0, "ipv6_max_prefixes": 0},
                "updates": {"ipv4_max_prefixes": None, "ipv6_max_prefixes": None},
            },
            "DirectPeeringSession": {
                "filters": {"advertised_prefix_count": 0, "received_prefix_count": 0},
                "updates": {
                    "advertised_prefix_count": None,
                    "received_prefix_count": None,
                },
            },
            "InternetExchange": {
                "filters": {"peeringdb_id": 0},
                "updates": {"peeringdb_id": None},
            },
            "InternetExchangePeeringSession": {
                "filters": {"advertised_prefix_count": 0, "received_prefix_count": 0},
                "updates": {
                    "advertised_prefix_count": None,
                    "received_prefix_count": None,
                },
            },
        }
        db_alias = schema_editor.connection.alias
        for key, value in models:
            model = apps.get_model("peering", key)
            for field in value:
                model.objects.using(db_alias).filter(**value["filters"]).update(
                    **value["updates"]
                )

    dependencies = [("peering", "0023_auto_20181208_2202")]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
        migrations.AlterField(
            model_name="autonomoussystem",
            name="ipv4_max_prefixes",
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="autonomoussystem",
            name="ipv6_max_prefixes",
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="directpeeringsession",
            name="advertised_prefix_count",
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="directpeeringsession",
            name="received_prefix_count",
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="internetexchange",
            name="peeringdb_id",
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="internetexchangepeeringsession",
            name="advertised_prefix_count",
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="internetexchangepeeringsession",
            name="received_prefix_count",
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
