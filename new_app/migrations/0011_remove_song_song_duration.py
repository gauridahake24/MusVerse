# Generated by Django 4.2.2 on 2023-07-13 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("new_app", "0010_alter_song_songaudio_file"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="song",
            name="song_duration",
        ),
    ]
