from django.db import models

class artist(models.Model):
    artist_id = models.AutoField(primary_key=True)
    artist_name = models.CharField(max_length=30)
    song_name = models.CharField(max_length=30)
    songaudio_file = models.FileField(upload_to='audio/')
    duration = models.DurationField(null=True, blank=True)

    def __str__(self):
        return self.artist_name

    def get_song_duration(self):
        if self.duration:
            return str(self.duration)
        else:
            return "Unknown"

    def get_file_url(self):
        return self.songaudio_file.url

# class user(models.Model):
#     userid = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=30)
#     mobile_no = models.BigIntegerField()
#     email = models.CharField(max_length=30)
#     country = models.CharField(max_length=50)
#     liked_songs = models.ManyToManyField(song)
#     playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)

# class guest(models.Model):
#     guestid = models.AutoField(primary_key=True)




# class song(models.Model):
#     song_id= models.AutoField(primary_key=True)
#     song_artist = models.CharField(max_length=30)
#     song_duration = models.DecimalField(max_digits=5, decimal_places=2)
#     popularity = models.BigIntegerField()

# class playlist(models.Model):
#     playlist_id = models.AutoField(primary_key=True)
#     User = models.ForeignKey(user, on_delete=models.CASCADE)
#     song = models.ForeignKey(song, on_delete=models.CASCADE)
#     playlist_name = models.CharField(max_length=30)
#     total_hours = models.BigIntegerField()
#     total_songs = models.BigIntegerField()
