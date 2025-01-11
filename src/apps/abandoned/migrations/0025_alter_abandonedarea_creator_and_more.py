# Generated by Django 5.1.2 on 2024-12-08 09:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("abandoned", "0024_abandonedobject_short_description_and_more"),
        ("media", "0003_alter_file_created_at_alter_file_creator_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="abandonedarea",
            name="creator",
            field=models.ForeignKey(
                blank=True,
                help_text="",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="areas",
                to=settings.AUTH_USER_MODEL,
                verbose_name="creator",
            ),
        ),
        migrations.AlterField(
            model_name="abandonedobject",
            name="creator",
            field=models.ForeignKey(
                blank=True,
                help_text="",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="abandoned_objects",
                to=settings.AUTH_USER_MODEL,
                verbose_name="creator",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="organizer",
            field=models.ForeignKey(
                help_text="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="my_events",
                to=settings.AUTH_USER_MODEL,
                verbose_name="organizer",
            ),
        ),
        migrations.AlterField(
            model_name="participation",
            name="event",
            field=models.ForeignKey(
                help_text="",
                on_delete=django.db.models.deletion.CASCADE,
                to="abandoned.event",
                verbose_name="event",
            ),
        ),
        migrations.AlterField(
            model_name="participation",
            name="user",
            field=models.ForeignKey(
                help_text="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="participations",
                to=settings.AUTH_USER_MODEL,
                verbose_name="user",
            ),
        ),
        migrations.CreateModel(
            name="AbandonedObjectFile",
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
                ("priority", models.IntegerField(default=0)),
                (
                    "file",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="media.file"
                    ),
                ),
                (
                    "object",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="abandoned.abandonedobject",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="abandonedobject",
            name="files",
            field=models.ManyToManyField(
                help_text="The media files representing this object.",
                related_name="abandoned_objects",
                through="abandoned.AbandonedObjectFile",
                to="media.file",
                verbose_name="files",
            ),
        ),
    ]