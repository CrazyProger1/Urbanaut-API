# Generated by Django 5.1.1 on 2024-09-28 14:39

import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_teammember_team_alter_teammember_user_and_more"),
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
        migrations.AlterField(
            model_name="user",
            name="born_at",
            field=models.DateField(
                blank=True,
                default=None,
                help_text="",
                null=True,
                verbose_name="Birth Date",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                blank=True, help_text="", max_length=254, verbose_name="Email Address"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                blank=True, help_text="", max_length=150, verbose_name="First Name"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="joined_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                help_text="",
                verbose_name="Joined At",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(
                blank=True, help_text="", max_length=150, verbose_name="Last Name"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(
                blank=True,
                help_text="",
                max_length=150,
                null=True,
                validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                verbose_name="Username",
            ),
        ),
    ]
