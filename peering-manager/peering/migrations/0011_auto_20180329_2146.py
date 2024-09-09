# Generated by Django 2.0.3 on 2018-03-29 19:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("peering", "0010_auto_20171228_0158")]

    operations = [
        migrations.AddField(
            model_name="autonomoussystem",
            name="keep_synced_with_peeringdb",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="peeringsession",
            name="enabled",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="router",
            name="platform",
            field=models.CharField(
                blank=True,
                choices=[
                    ("junos", "Juniper JUNOS"),
                    ("iosxr", "Cisco IOS-XR"),
                    ("ios", "Cisco IOS"),
                    ("nxos", "Cisco NX-OS"),
                    ("eos", "Arista EOS"),
                    (None, "Other"),
                ],
                help_text="The router platform, used to interact with it",
                max_length=50,
            ),
        ),
    ]
