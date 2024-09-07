# Generated by Django 5.1.1 on 2024-09-07 17:25

import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0009_notification_message_en_notification_message_uk_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="show_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                help_text="Planned time to show.",
                verbose_name="Show At",
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="message",
            field=models.TextField(help_text="", verbose_name="Message"),
        ),
        migrations.AlterField(
            model_name="notification",
            name="message_en",
            field=models.TextField(help_text="", null=True, verbose_name="Message"),
        ),
        migrations.AlterField(
            model_name="notification",
            name="message_uk",
            field=models.TextField(help_text="", null=True, verbose_name="Message"),
        ),
        migrations.AlterField(
            model_name="notification",
            name="recipients",
            field=models.ManyToManyField(
                help_text="",
                through="accounts.NotificationStatus",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Recipients",
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="title",
            field=models.CharField(help_text="", max_length=150, verbose_name="Title"),
        ),
        migrations.AlterField(
            model_name="notification",
            name="title_en",
            field=models.CharField(
                help_text="", max_length=150, null=True, verbose_name="Title"
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="title_uk",
            field=models.CharField(
                help_text="", max_length=150, null=True, verbose_name="Title"
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
                to="accounts.notification",
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
