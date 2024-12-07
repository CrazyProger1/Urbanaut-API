# Generated by Django 5.1.2 on 2024-12-07 21:11

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("geo", "0022_alter_location_options_alter_location_point"),
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
