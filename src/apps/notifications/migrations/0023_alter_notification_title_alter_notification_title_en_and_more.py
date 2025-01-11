# Generated by Django 5.1.2 on 2024-12-07 21:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "notifications",
            "0022_alter_notification_options_alter_notification_icon_and_more",
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
                to="notifications.notification",
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
