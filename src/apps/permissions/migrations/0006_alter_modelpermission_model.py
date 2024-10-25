# Generated by Django 5.1.1 on 2024-10-06 13:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("permissions", "0005_alter_modelpermission_changebility_level_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="modelpermission",
            name="model",
            field=models.ForeignKey(
                help_text="The name of the model you would like to add permissions for.",
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.contenttype",
                unique=True,
                verbose_name="Model Name",
            ),
        ),
    ]
