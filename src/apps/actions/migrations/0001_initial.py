# Generated by Django 5.1.1 on 2024-09-28 11:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Action",
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
                (
                    "type",
                    models.CharField(
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
                        verbose_name="Type",
                    ),
                ),
                (
                    "data",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        help_text="Action additional data.",
                        null=True,
                        verbose_name="Data",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="User who made the action.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Action",
                "verbose_name_plural": "Actions",
            },
        ),
    ]