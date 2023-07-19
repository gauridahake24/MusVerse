from django.shortcuts import render, reverse , redirect
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from .models import User
from .models import Artist
from datetime import timedelta
import magic
from .models import Song
import boto3
from django.conf import settings
from botocore.exceptions import ClientError
from requests_aws4auth import AWS4Auth
import requests
import logging
# Create your views here.
def home(request):
    global context
    context = {}
    if 'login_status' in request.COOKIES and 'username' in request.COOKIES:
        context['login_status'] = request.COOKIES.get('login_status')
        context['username'] = request.COOKIES['username']
        return render(request, "home.html", context)

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if len(User.objects.filter(email = email))!=0:
            arr = User.objects.filter(email = email)[0]
            context['username'] = arr.username
            print(context['username'])
            context['name'] = arr.username
            context['id'] = arr.userid
            print(context['name'])
        
    return render(request, "home.html", context)
logger = logging.getLogger(__name__)

def upload_audio_to_s3(file, s3_key):
    s3 = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
    )
    try:
        s3.upload_fileobj(file, settings.AWS_STORAGE_BUCKET_NAME, s3_key)
        return True
    except Exception as e:
        logger.error(f"Error uploading audio to S3: {e}")
        return False

def artist(request):
    if request.method == 'POST':
        artist_name = request.POST.get('artist_name')
        song_name = request.POST.get('song_name')
        songaudio_file = request.FILES.get('songaudio_file')
        duration = request.POST.get('duration')

        # Check if the uploaded file is empty
        if not songaudio_file:
            return render(request, "error.html", {'error_message': 'No audio file selected.'})

        # Save the Artist object
        artist, created = Artist.objects.get_or_create(artist_name=artist_name)

        # Save the Song object
        song = Song.objects.create(
            song_artist=artist,
            song_name=song_name,
            popularity=0,
            songaudio_file_urn=duration  # You can change this field to store the duration if needed.
        )

        # Upload audio file to S3
        s3_key = f'audio/{songaudio_file.name}'
        if upload_audio_to_s3(songaudio_file, s3_key):
            song.songaudio_file_urn = s3_key
            song.save()
        else:
            # Handle the case when the audio file upload to S3 fails
            song.delete()
            return render(request, "error.html", {'error_message': 'Error uploading audio to S3.'})

        return redirect('artist_page')  # Replace 'artist_page' with the URL name of the page you want to redirect to after successful submission

    return render(request, "artist_page.html")  # Replace 'artist_form' with the name of your template for the artist form
def test(request):
    return render(request, "test.html")

    
def albums(request):
    return render(request, "albums.html")

def playlist(request):
    return HttpResponse("hello this is playlist")

def liked_songs(request):
    return HttpResponse("hello this is liked songs")

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # password = request.POST.get('password')
        if len(User.objects.filter(email = email))!=0:
            arr = User.objects.filter(email = email)[0]
            context['username'] = arr.username
            context['id'] = arr.userid
    
            response = render(request, 'home.html', context)
            response.set_cookie('username', arr.username)
            response.set_cookie('login_status', True)
            return response
    return render(request, "log_in.html")

def logout(request):
    response = HttpResponseRedirect(reverse('login'))
    response.delete_cookie('username')
    response.delete_cookie('login_status')

    return response

def search(request):
    context = {}

    if request.method == 'POST':
        val = request.POST.get('val')
        count = 1
        if len(Song.objects.filter(song_name__icontains = val).order_by('-popularity'))!=0:
            context['data'] = []
            arr = Song.objects.filter(song_name__icontains = val).order_by('-popularity')
            for i in arr:
                temp = {"Song": i.song_name, "Artist": i.song_artist, "Popularity": i.popularity}
                context['data'].append(temp)
            print(context)
            return render(request, "search.html", context)
    

    return render(request, "search.html")
# Create your views here.
