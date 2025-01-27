# Generated by Django 5.1.1 on 2024-09-28 14:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("media", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="file",
            name="is_hidden",
            field=models.BooleanField(
                default=False,
                help_text="Hidden from general users and available only for admins and creator.",
                verbose_name="Hidden",
            ),
        ),
        migrations.AlterField(
            model_name="file",
            name="creator",
            field=models.ForeignKey(
                blank=True,
                help_text="User who uploaded the file.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="files",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Creator",
            ),
        ),
        migrations.AlterField(
            model_name="file",
            name="file",
            field=models.FileField(
                help_text="Uploaded file.", upload_to="uploads/", verbose_name="File"
            ),
        ),
    ]
