# Generated by Django 5.1.1 on 2024-09-07 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("abandoned", "0004_remove_event_end_datetime_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="abandonedobject",
            old_name="hidden",
            new_name="is_hidden",
        ),
    ]