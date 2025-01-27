# Generated by Django 5.1.2 on 2024-12-07 20:14

import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0022_alter_teammember_team_alter_teammember_user"),
        ("media", "0003_alter_file_created_at_alter_file_creator_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="team",
            options={"verbose_name": "team", "verbose_name_plural": "teams"},
        ),
        migrations.AlterModelOptions(
            name="teammember",
            options={
                "verbose_name": "team member",
                "verbose_name_plural": "team members",
            },
        ),
        migrations.AlterField(
            model_name="team",
            name="name",
            field=models.CharField(
                help_text="Name of the team.",
                max_length=250,
                unique=True,
                verbose_name="name",
            ),
        ),
        migrations.AlterField(
            model_name="teammember",
            name="team",
            field=models.ForeignKey(
                help_text="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="members",
                to="accounts.team",
                verbose_name="team",
            ),
        ),
        migrations.AlterField(
            model_name="teammember",
            name="user",
            field=models.ForeignKey(
                help_text="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="members",
                to=settings.AUTH_USER_MODEL,
                verbose_name="user",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ForeignKey(
                blank=True,
                help_text="The avatar of the user.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="media.file",
                verbose_name="avatar",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="born_at",
            field=models.DateField(
                blank=True,
                default=None,
                help_text="User born at date and time.",
                null=True,
                verbose_name="birth Date",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                blank=True,
                help_text="Email address of the user.",
                max_length=254,
                verbose_name="email address",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="experience",
            field=models.PositiveIntegerField(
                default=0,
                help_text="The experience of the user.",
                verbose_name="experience",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                blank=True,
                help_text="First name in telegram.",
                max_length=150,
                verbose_name="first name",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.BigIntegerField(
                help_text="Telegram user ID",
                primary_key=True,
                serialize=False,
                verbose_name="telegram ID",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                verbose_name="active",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(
                default=False,
                help_text="Designates whether the user can log into this admin site.",
                verbose_name="staff status",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="joined_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                help_text="User joined at date and time.",
                verbose_name="joined at",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="karma",
            field=models.IntegerField(
                default=0, help_text="The karma of the user.", verbose_name="karma"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="language",
            field=models.CharField(
                choices=[("en", "English"), ("uk", "Ukrainian")],
                default="en",
                help_text="Preferred language of the user.",
                max_length=10,
                verbose_name="language",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(
                blank=True,
                help_text="Last name in telegram.",
                max_length=150,
                verbose_name="last name",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="nickname",
            field=models.CharField(
                blank=True,
                help_text="Nickname of the user.",
                max_length=150,
                null=True,
                verbose_name="nickname",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="rank",
            field=models.CharField(
                choices=[("NEWBIE", "NEWBIE")],
                default="NEWBIE",
                help_text="The rank of the user.",
                verbose_name="rank",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True,
                help_text="User updated date and time.",
                verbose_name="updated at",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(
                blank=True,
                help_text="Telegram username.",
                max_length=150,
                null=True,
                validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                verbose_name="username",
            ),
        ),
    ]
