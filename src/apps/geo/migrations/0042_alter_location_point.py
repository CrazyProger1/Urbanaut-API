# Generated by Django 5.0.8 on 2025-02-11 20:05

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("geo", "0041_alter_location_point"),
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
