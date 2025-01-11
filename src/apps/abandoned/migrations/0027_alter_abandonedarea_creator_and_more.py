# Generated by Django 5.1.2 on 2024-12-16 10:43

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("abandoned", "0026_alter_abandonedobjectfile_options_and_more"),
        ("permissions", "0007_alter_modelpermission_changebility_level_and_more"),
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
            name="AbandonedObjectCategory",
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
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text="Object creation date and time.",
                        verbose_name="created at",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Object updated date and time.",
                        verbose_name="updated at",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Name of the object category.",
                        max_length=250,
                        verbose_name="name",
                    ),
                ),
                (
                    "name_en",
                    models.CharField(
                        help_text="Name of the object category.",
                        max_length=250,
                        null=True,
                        verbose_name="name",
                    ),
                ),
                (
                    "name_uk",
                    models.CharField(
                        help_text="Name of the object category.",
                        max_length=250,
                        null=True,
                        verbose_name="name",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Description of the object category.",
                        null=True,
                        verbose_name="description",
                    ),
                ),
                (
                    "description_en",
                    models.TextField(
                        blank=True,
                        help_text="Description of the object category.",
                        null=True,
                        verbose_name="description",
                    ),
                ),
                (
                    "description_uk",
                    models.TextField(
                        blank=True,
                        help_text="Description of the object category.",
                        null=True,
                        verbose_name="description",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        help_text="",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="categories",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="creator",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        help_text="Parent category.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="abandoned.abandonedobjectcategory",
                        verbose_name="parent category",
                    ),
                ),
                (
                    "permissions",
                    models.OneToOneField(
                        blank=True,
                        help_text="Blog post permissions.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="permissions.objectpermission",
                        verbose_name="permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "category",
                "verbose_name_plural": "categories",
            },
        ),
    ]