# Generated by Django 4.2.2 on 2023-07-09 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("new_app", "0003_alter_user_email"),
    ]

    operations = [
        migrations.RenameField(
            model_name="artist",
            old_name="duration",
            new_name="duration_str",
        ),
    ]
