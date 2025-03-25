# Generated by Django 5.0.8 on 2025-02-11 19:35

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0033_alter_teammember_team_alter_teammember_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Rank",
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
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text="Creation date and time.",
                        verbose_name="created at",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Update date and time.",
                        verbose_name="updated at",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="The name of the rank.",
                        max_length=255,
                        unique=True,
                        verbose_name="name",
                    ),
                ),
            ],
            options={
                "verbose_name": "Rank",
                "verbose_name_plural": "Ranks",
            },
        ),
        migrations.AlterField(
            model_name="teammember",
            name="team",
            field=models.ForeignKey(
                help_text="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="members",
                to="accounts.team",
                verbose_name="team",
            ),
        ),
        migrations.AlterField(
            model_name="teammember",
            name="user",
            field=models.ForeignKey(
                help_text="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="members",
                to=settings.AUTH_USER_MODEL,
                verbose_name="user",
            ),
        ),
    ]
