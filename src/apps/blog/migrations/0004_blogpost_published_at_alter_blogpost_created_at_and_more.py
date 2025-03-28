# Generated by Django 5.1.1 on 2024-09-29 09:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_blogtopic_is_closed"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="published_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                help_text="Post published (or planned publishing) date and time.",
                verbose_name="Published At",
            ),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="created_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                help_text="Post creation date and time.",
                verbose_name="Created At",
            ),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True,
                help_text="Post updated date and time.",
                verbose_name="Updated At",
            ),
        ),
    ]
