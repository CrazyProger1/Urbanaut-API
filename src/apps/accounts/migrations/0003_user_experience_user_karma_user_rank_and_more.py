# Generated by Django 5.1.1 on 2024-09-07 14:23

import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_user_options_alter_user_managers_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="experience",
            field=models.PositiveIntegerField(
                default=0,
                help_text="The experience of the user.",
                verbose_name="Experience",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="karma",
            field=models.IntegerField(
                default=0, help_text="The karma of the user.", verbose_name="Karma"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="rank",
            field=models.CharField(
                choices=[("NEWBIE", "NEWBIE")],
                default="NEWBIE",
                help_text="The rank of the user.",
                verbose_name="Rank",
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
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                verbose_name="Active",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(
                default=False,
                help_text="Designates whether the user can log into this admin site.",
                verbose_name="Staff Status",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="joined_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Joined At"
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
