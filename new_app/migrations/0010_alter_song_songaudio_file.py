# Generated by Django 4.2.2 on 2023-07-13 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("new_app", "0009_remove_artist_duration_str_remove_artist_song_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="song",
            name="songaudio_file",
            field=models.FileField(upload_to="audio/"),
        ),
    ]
