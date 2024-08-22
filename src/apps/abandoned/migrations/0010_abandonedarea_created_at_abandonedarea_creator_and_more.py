# Generated by Django 5.1 on 2024-08-22 06:47

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("abandoned", "0009_abandonedobject_abandoned_at_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="abandonedarea",
            name="created_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                help_text="Object creation date and time.",
                verbose_name="Created At",
            ),
        ),
        migrations.AddField(
            model_name="abandonedarea",
            name="creator",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="areas",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Creator",
            ),
        ),
        migrations.AddField(
            model_name="abandonedarea",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="Description of the abandoned area.",
                null=True,
                verbose_name="Description",
            ),
        ),
        migrations.AddField(
            model_name="abandonedarea",
            name="security_level",
            field=models.CharField(
                choices=[("NONE", "NONE")],
                default="NONE",
                help_text="Security level of the area.",
                max_length=50,
                verbose_name="Security Level",
            ),
        ),
        migrations.AddField(
            model_name="abandonedarea",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True,
                help_text="Object updated date and time.",
                verbose_name="Updated At",
            ),
        ),
        migrations.AlterField(
            model_name="abandonedobject",
            name="abandoned_at",
            field=models.DateField(
                blank=True,
                help_text="When object became abandoned date and time.",
                null=True,
                verbose_name="Abandoned At",
            ),
        ),
    ]
