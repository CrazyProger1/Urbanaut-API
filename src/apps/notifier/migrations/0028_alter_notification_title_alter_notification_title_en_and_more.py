# Generated by Django 5.1.4 on 2025-01-12 12:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "notifier",
            "0027_alter_notification_title_alter_notification_title_en_and_more",
        ),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="title",
            field=models.CharField(help_text="", max_length=150, verbose_name="title"),
        ),
        migrations.AlterField(
            model_name="notification",
            name="title_en",
            field=models.CharField(
                help_text="", max_length=150, null=True, verbose_name="title"
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="title_uk",
            field=models.CharField(
                help_text="", max_length=150, null=True, verbose_name="title"
            ),
        ),
        migrations.AlterField(
            model_name="notificationstatus",
            name="is_read",
            field=models.BooleanField(default=False, help_text="", verbose_name="Read"),
        ),
        migrations.AlterField(
            model_name="notificationstatus",
            name="notification",
            field=models.ForeignKey(
                help_text="",
                on_delete=django.db.models.deletion.CASCADE,
                to="notifier.notification",
                verbose_name="Notification",
            ),
        ),
        migrations.AlterField(
            model_name="notificationstatus",
            name="user",
            field=models.ForeignKey(
                help_text="",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Recipient",
            ),
        ),
    ]
