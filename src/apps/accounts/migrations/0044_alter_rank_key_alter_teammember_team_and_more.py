# Generated by Django 5.0.8 on 2025-02-13 19:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0043_alter_teammember_team_alter_teammember_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rank",
            name="key",
            field=models.CharField(max_length=20, unique=True),
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
