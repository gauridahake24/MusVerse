import boto3
from botocore.exceptions import ClientError
from django.conf import settings
from django.db import models
from django.utils import timezone

class Artist(models.Model):
    artist_id = models.AutoField(primary_key=True)
    artist_name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.artist_name)


    def get_song_duration(self):
        if self.duration:
            return str(self.duration)
        else:
            return "Unknown"



class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    song_artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='uploaded_songs')
    song_name = models.CharField(max_length=30)
    # song_duration = models.DecimalField(max_digits=5, decimal_places=2)
    popularity = models.BigIntegerField()
    songaudio_file_urn = models.CharField(max_length=255, default=timezone.now)

    def __str__(self):
        return f"Song: {self.song_id}, Artist: {self.song_artist}"
    
    def save(self, *args, **kwargs):
        if self.songaudio_file_urn:
            # You don't need to read from songaudio_file_urn because it's just a URL string.
            # The file content has been read earlier in the view before uploading to S3.
            try:
                s3_resource = boto3.resource(
                    's3',
                    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
                )
                # Instead, use the songaudio_file_urn directly to generate the object URL
                obj_url = s3_resource.meta.client.generate_presigned_url(
                    'get_object',
                    Params={'Bucket': settings.AWS_STORAGE_BUCKET_NAME, 'Key': self.songaudio_file_urn},
                    ExpiresIn=3600
                )
                self.songaudio_file_urn = obj_url
            except ClientError as e:
                # Handle any errors that might occur during URL generation
                raise e

        # Call the original save method to save the Song object to the database
        super(Song, self).save(*args, **kwargs)



class User(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    mobile_no = models.BigIntegerField()
    email = models.CharField(max_length=70)
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
