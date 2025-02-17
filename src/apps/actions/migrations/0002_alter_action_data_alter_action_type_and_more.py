# Generated by Django 5.1.2 on 2024-12-07 20:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("actions", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="action",
            name="data",
            field=models.JSONField(
                blank=True,
                default=dict,
                help_text="Action additional data.",
                null=True,
                verbose_name="data",
            ),
        ),
        migrations.AlterField(
            model_name="action",
            name="type",
            field=models.CharField(
                choices=[
                    ("REGISTERED", "REGISTERED"),
                    ("LOGGED IN", "LOGGED IN"),
                    ("LOGGED OUT", "LOGGED OUT"),
                    ("CREATED ABANDONED OBJECT", "CREATED ABANDONED OBJECT"),
                    ("CREATED ABANDONED AREA", "CREATED ABANDONED AREA"),
                    ("UPDATED ABANDONED OBJECT", "UPDATED ABANDONED OBJECT"),
                    ("UPDATED ABANDONED AREA", "UPDATED ABANDONED AREA"),
                ],
                help_text="Type of an action.",
                verbose_name="type",
            ),
        ),
        migrations.AlterField(
            model_name="action",
            name="user",
            field=models.ForeignKey(
                help_text="User who made the action.",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="user",
            ),
        ),
    ]
