# Generated by Django 5.1.2 on 2024-12-07 21:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0023_alter_team_options_alter_teammember_options_and_more"),
    ]

    operations = [
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
