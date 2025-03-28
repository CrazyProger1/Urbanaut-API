# Generated by Django 5.0.8 on 2025-02-17 20:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("abandoned", "0045_alter_abandonedarea_creator_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="abandonedarea",
            name="creator",
        ),
        migrations.RemoveField(
            model_name="abandonedobject",
            name="creator",
        ),
        migrations.RemoveField(
            model_name="category",
            name="creator",
        ),
        migrations.AddField(
            model_name="abandonedarea",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                help_text="",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="areas",
                to=settings.AUTH_USER_MODEL,
                verbose_name="created by",
            ),
        ),
        migrations.AddField(
            model_name="abandonedobject",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                help_text="",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="abandoned_objects",
                to=settings.AUTH_USER_MODEL,
                verbose_name="created by",
            ),
        ),
        migrations.AddField(
            model_name="category",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                help_text="",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="categories",
                to=settings.AUTH_USER_MODEL,
                verbose_name="created by",
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
    ]
