# Generated by Django 5.1.1 on 2024-09-28 14:51

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("geo", "0003_alter_location_point"),
    ]

    operations = [
        migrations.AlterField(
            model_name="location",
            name="point",
            field=django.contrib.gis.db.models.fields.PointField(
                help_text="", srid=4326, unique=True, verbose_name="Point"
            ),
        ),
    ]
