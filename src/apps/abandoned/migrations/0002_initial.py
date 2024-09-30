# Generated by Django 5.1.1 on 2024-09-28 11:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("abandoned", "0001_initial"),
        ("geo", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
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
        migrations.AddField(
            model_name="abandonedobject",
            name="area",
            field=models.ForeignKey(
                blank=True,
                help_text="Area that contains current object.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="abandoned_objects",
                to="abandoned.abandonedarea",
                verbose_name="Area",
            ),
        ),
        migrations.AddField(
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
        migrations.AddField(
            model_name="abandonedobject",
            name="location",
            field=models.ForeignKey(
                blank=True,
                help_text="Location of the object.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="objects",
                to="geo.location",
                verbose_name="Location",
            ),
        ),
        migrations.AddField(
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
        migrations.AddField(
            model_name="participation",
            name="event",
            field=models.ForeignKey(
                help_text="",
                on_delete=django.db.models.deletion.CASCADE,
                to="abandoned.event",
                verbose_name="Event",
            ),
        ),
        migrations.AddField(
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
        migrations.AddField(
            model_name="event",
            name="participants",
            field=models.ManyToManyField(
                help_text="Users that participate in this trip.",
                related_name="events",
                through="abandoned.Participation",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Participants",
            ),
        ),
        migrations.AddField(
            model_name="participationreport",
            name="participation",
            field=models.ForeignKey(
                help_text="Report destination participation.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reports",
                to="abandoned.participation",
                verbose_name="Participation",
            ),
        ),
    ]