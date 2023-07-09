from django.db import models

class artist(models.Model):
    artist_id = models.AutoField(primary_key=True)
    artist_name = models.CharField(max_length=30)
    song_name = models.CharField(max_length=30)
    songaudio_file = models.FileField(upload_to='audio/')
    duration = models.DurationField(null=True, blank=True)

    def __str__(self):
        return str(self.artist_id)

    def __str__(self):
        return self.artist_name

    def get_song_duration(self):
        if self.duration:
            return str(self.duration)
        else:
            return "Unknown"

    def get_file_url(self):
        return self.songaudio_file.url


from django.db import models

class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    song_artist = models.CharField(max_length=30)
    song_duration = models.DecimalField(max_digits=5, decimal_places=2)
    popularity = models.BigIntegerField()

    def __str__(self):
        return f"Song: {self.song_id}, Artist: {self.song_artist}"


class User(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    mobile_no = models.BigIntegerField()
    email = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    liked_songs = models.ManyToManyField(Song)

    def add_liked_song(self, song):
        self.liked_songs.add(song)

    def remove_liked_song(self, song):
        self.liked_songs.remove(song)

    def get_liked_songs(self):
        return self.liked_songs.all()

    def get_song_count(self):
        return self.liked_songs.count()

    def __str__(self):
        return self.username
    
    def __str__(self):
        return str(self.userid)



# class guest(models.Model):
#     guestid = models.AutoField(primary_key=True)




# class playlist(models.Model):
#     playlist_id = models.AutoField(primary_key=True)
#     User = models.ForeignKey(user, on_delete=models.CASCADE)
#     song = models.ForeignKey(song, on_delete=models.CASCADE)
#     playlist_name = models.CharField(max_length=30)
#     total_hours = models.BigIntegerField()
#     total_songs = models.BigIntegerField()


# Create your models here.


# Create your models here.