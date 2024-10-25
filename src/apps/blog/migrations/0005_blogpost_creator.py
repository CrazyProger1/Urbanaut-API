# Generated by Django 5.1.1 on 2024-09-29 12:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_blogpost_published_at_alter_blogpost_created_at_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="creator",
            field=models.ForeignKey(
                blank=True,
                help_text="Creator of the blog post.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="blog_posts",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Creator",
            ),
        ),
    ]
