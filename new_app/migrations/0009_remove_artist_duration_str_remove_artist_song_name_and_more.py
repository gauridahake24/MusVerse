# Generated by Django 4.2.2 on 2023-07-12 17:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("new_app", "0008_auto_20230712_2305"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="artist",
            name="duration_str",
        ),
        migrations.RemoveField(
            model_name="artist",
            name="song_name",
        ),
        migrations.RemoveField(
            model_name="artist",
            name="songaudio_file",
        ),
        migrations.AddField(
            model_name="song",
            name="songaudio_file",
            field=models.FileField(
                default=django.utils.timezone.now, upload_to="audio/"
            ),
        ),
        migrations.AlterField(
            model_name="song",
            name="song_artist",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="uploaded_songs",
                to="new_app.artist",
            ),
        ),
    ]
