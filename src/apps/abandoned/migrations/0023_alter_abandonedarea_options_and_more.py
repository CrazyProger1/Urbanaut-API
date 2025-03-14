# Generated by Django 5.1.2 on 2024-12-07 20:14

import django.db.models.deletion
import django.utils.timezone
import mdeditor.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("abandoned", "0022_remove_abandonedarea_is_hidden_and_more"),
        ("geo", "0022_alter_location_options_alter_location_point"),
        ("permissions", "0006_alter_modelpermission_model"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="abandonedarea",
            options={"verbose_name": "area", "verbose_name_plural": "areas"},
        ),
        migrations.AlterModelOptions(
            name="abandonedobject",
            options={"verbose_name": "object", "verbose_name_plural": "objects"},
        ),
        migrations.AlterModelOptions(
            name="event",
            options={"verbose_name": "event", "verbose_name_plural": "events"},
        ),
        migrations.AlterModelOptions(
            name="participation",
            options={
                "verbose_name": "participation",
                "verbose_name_plural": "participations",
            },
        ),
        migrations.AlterModelOptions(
            name="participationreport",
            options={"verbose_name": "report", "verbose_name_plural": "reports"},
        ),
        migrations.AlterField(
            model_name="abandonedarea",
            name="area",
            field=models.ForeignKey(
                blank=True,
                help_text="Area that contains current area.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="areas",
                to="abandoned.abandonedarea",
                verbose_name="parent area",
            ),
        ),
        migrations.AlterField(
            model_name="abandonedarea",
            name="created_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                help_text="Object creation date and time.",
                verbose_name="created at",
            ),
        ),
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
            model_name="abandonedarea",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="Description of the abandoned area.",
                null=True,
                verbose_name="description",
            ),
        ),
        migrations.AlterField(
            model_name="abandonedarea",
            name="description_en",
            field=models.TextField(
                blank=True,
                help_text="Description of the abandoned area.",
                null=True,
                verbose_name="description",
            ),
        ),
        migrations.AlterField(
            model_name="abandonedarea",
            name="description_uk",
            field=models.TextField(
                blank=True,
                help_text="Description of the abandoned area.",
                null=True,
                verbose_name="description",
            ),
        ),
        migrations.AlterField(
            model_name="abandonedarea",
            name="name",
            field=models.CharField(
                help_text="Name of the abandoned area.",
                max_length=250,
                verbose_name="name",
            ),
        ),
        migrations.AlterField(
            model_name="abandonedarea",
            name="name_en",
            field=models.CharField(
                help_text="Name of the abandoned area.",
                max_length=250,
                null=True,
                verbose_name="name",
            ),
        ),
        migrations.AlterField(
            model_name="abandonedarea",
            name="name_uk",
            field=models.CharField(
                help_text="Name of the abandoned area.",
                max_length=250,
                null=True,
                verbose_name="name",
            ),
        ),
        migrations.AlterField(
            model_name="abandonedarea",
            name="permissions",
            field=models.OneToOneField(
                blank=True,
                help_text="Blog post permissions.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="permissions.objectpermission",
                verbose_name="permissions",
            ),
        ),
        migrations.AlterField(
            model_name="abandonedarea",
            name="security_level",
            field=models.CharField(
                choices=[("NONE", "NONE")],
                default="NONE",
                help_text="security level of the area.",
                verbose_name="security level",
            ),
        ),
        migrations.AlterField(
            model_name="abandonedarea",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True,
                help_text="Object updated date and time.",
                verbose_name="updated at",
            ),
        ),
        migrations.AlterField(
            model_name="abandonedobject",
            name="abandoned_at",
            field=models.DateField(
                blank=True,
                help_text="When object became abandoned date and time.",
                null=True,
                verbose_name="abandoned at",
            ),
        ),
        migrations.AlterField(
            model_name="abandonedobject",
            name="area",
            field=models.ForeignKey(
                blank=True,
                help_text="Area that contains current object.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="abandoned_objects",
                to="abandoned.abandonedarea",
                verbose_name="area",
            ),
        ),
        migrations.AlterField(
            model_name="abandonedobject",
            name="built_at",
            field=models.DateField(
                blank=True,
                help_text="Object built date and time.",
                null=True,
                verbose_name="built at",
            ),
        ),
        migrations.AlterField(
            model_name="abandonedobject",
            name="created_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                help_text="Object creation date and time.",
                verbose_name="created at",
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
            model_name="abandonedobject",
            name="description",
            field=mdeditor.fields.MDTextField(
                blank=True,
                help_text="Description of the abandoned object.",
                null=True,
                verbose_name="description",
            ),
        ),
        migrations.AlterField(
            model_name="abandonedobject",
            name="description_en",
            field=mdeditor.fields.MDTextField(
                blank=True,
                help_text="Description of the abandoned object.",
                null=True,
                verbose_name="description",
            ),
        ),
        migrations.AlterField(
            model_name="abandonedobject",
            name="description_uk",
            field=mdeditor.fields.MDTextField(
                blank=True,
                help_text="Description of the abandoned object.",
                null=True,
                verbose_name="description",
            ),
        ),
        migrations.AlterField(
            model_name="abandonedobject",
            name="difficulty_level",
            field=models.CharField(
                choices=[
                    ("NEWBIE", "NEWBIE"),
                    ("EASY", "EASY"),
                    ("MEDIUM", "MEDIUM"),
                    ("HIGH", "HIGH"),
                ],
                default="NEWBIE",
                help_text="Difficulty level of the object.",
                verbose_name="difficulty level",
            ),
        ),
        migrations.AlterField(
            model_name="abandonedobject",
            name="location",
            field=models.ForeignKey(
                blank=True,
                help_text="Location of the object.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="objects",
                to="geo.location",
                verbose_name="location",
            ),
        ),
        migrations.AlterField(
            model_name="abandonedobject",
            name="name",
            field=models.CharField(
                help_text="Name of the abandoned object.",
                max_length=250,
                verbose_name="name",
            ),
        ),
        migrations.AlterField(
            model_name="abandonedobject",
            name="name_en",
            field=models.CharField(
                help_text="Name of the abandoned object.",
                max_length=250,
                null=True,
                verbose_name="name",
            ),
        ),
        migrations.AlterField(
            model_name="abandonedobject",
            name="name_uk",
            field=models.CharField(
                help_text="Name of the abandoned object.",
                max_length=250,
                null=True,
                verbose_name="name",
            ),
        ),
        migrations.AlterField(
            model_name="abandonedobject",
            name="permissions",
            field=models.OneToOneField(
                blank=True,
                help_text="Blog post permissions.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="permissions.objectpermission",
                verbose_name="permissions",
            ),
        ),
        migrations.AlterField(
            model_name="abandonedobject",
            name="preservation_level",
            field=models.CharField(
                choices=[
                    ("LOW", "LOW"),
                    ("MEDIUM", "MEDIUM"),
                    ("HIGH", "HIGH"),
                    ("DANGEROUS", "DANGEROUS"),
                ],
                default="HIGH",
                help_text="Preservation level of the object.",
                verbose_name="preservation Level",
            ),
        ),
        migrations.AlterField(
            model_name="abandonedobject",
            name="security_level",
            field=models.CharField(
                choices=[("NONE", "NONE")],
                default="NONE",
                help_text="Security level of the object.",
                verbose_name="security Level",
            ),
        ),
        migrations.AlterField(
            model_name="abandonedobject",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True,
                help_text="Object updated date and time.",
                verbose_name="updated at",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                help_text="Event creation date and time.",
                verbose_name="created at",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="end_at",
            field=models.DateTimeField(
                help_text="Date and time of end of trip.", verbose_name="end at"
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="name",
            field=models.CharField(
                help_text="Name of the event.", max_length=250, verbose_name="name"
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="name_en",
            field=models.CharField(
                help_text="Name of the event.",
                max_length=250,
                null=True,
                verbose_name="name",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="name_uk",
            field=models.CharField(
                help_text="Name of the event.",
                max_length=250,
                null=True,
                verbose_name="name",
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
            model_name="event",
            name="participants",
            field=models.ManyToManyField(
                help_text="Users that participate in this trip.",
                related_name="events",
                through="abandoned.Participation",
                to=settings.AUTH_USER_MODEL,
                verbose_name="participants",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="start_at",
            field=models.DateTimeField(
                help_text="Date and time of start of trip.", verbose_name="start at"
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
        migrations.AlterField(
            model_name="participationreport",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                help_text="Report creation date and time.",
                verbose_name="created at",
            ),
        ),
        migrations.AlterField(
            model_name="participationreport",
            name="participation",
            field=models.ForeignKey(
                help_text="Report destination participation.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reports",
                to="abandoned.participation",
                verbose_name="participation",
            ),
        ),
    ]
