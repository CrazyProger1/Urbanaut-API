# Generated by Django 5.1.1 on 2024-09-28 14:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("abandoned", "0002_initial"),
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
                verbose_name="Creator",
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
                verbose_name="Creator",
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
                verbose_name="Organizer",
            ),
        ),
        migrations.AlterField(
            model_name="participation",
            name="event",
            field=models.ForeignKey(
                help_text="",
                on_delete=django.db.models.deletion.CASCADE,
                to="abandoned.event",
                verbose_name="Event",
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
                verbose_name="User",
            ),
        ),
    ]
