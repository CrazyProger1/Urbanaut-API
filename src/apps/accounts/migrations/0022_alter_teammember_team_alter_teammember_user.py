# Generated by Django 5.1.1 on 2024-10-06 18:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0021_alter_teammember_team_alter_teammember_user"),
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
                verbose_name="Team",
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
                verbose_name="User",
            ),
        ),
    ]
