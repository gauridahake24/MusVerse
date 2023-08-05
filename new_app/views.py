from django.shortcuts import render, reverse , redirect
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from .models import User
from .models import Artist, liked_songs
# from datetime import timedelta
# import magic
from .models import Song
# import boto3
from django.conf import settings
# from botocore.exceptions import ClientError
# from requests_aws4auth import AWS4Auth
# import requests
import logging
import os
from new_app import firebase_functions


# Create your views here.
def session_status(request):
    if 'login_status' in request.COOKIES and 'username' in request.COOKIES:
        context['login_status'] = request.COOKIES.get('login_status')
        context['username'] = request.COOKIES['username']

    


def home(request):
    global context
    context = {}
    session_status(request)

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


def liked_songs(request):
    if request.method == 'POST':
        song_id = request.POST.get('song_id')
        if song_id:
            # song = Song.objects.get(pk=song_id)
            # user = request.user
            # liked_song, created = LikedSong.objects.get_or_create(uid=user)
            # liked_song.liked_songs.add(song)
            return redirect('liked-songs')  
    return redirect('home') 



def delete_file(file_path):
    try:
        # Check if the file exists before attempting to delete
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File '{file_path}' deleted successfully.")
        else:
            print(f"File '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred while deleting the file: {e}")



def artist(request):
    session_status(request)
    if request.method == 'POST':

        data = {"Artist": request.POST.get('artist_name'),
                "Name": request.POST.get('song_name')
        }

        songaudio_file = request.FILES['songaudio_file']

        # Check if the uploaded file is empty
        if not songaudio_file:
            return render(request, "error.html", {'error_message': 'No audio file selected.'})

        # Save the Artist object
        # artist, created = Artist.objects.get_or_create(artist_name=artist_name)
        
        with open('media/' + songaudio_file.name, 'wb+') as destination_file:
            for chunk in songaudio_file.chunks():
                destination_file.write(chunk)
        
        firebase_functions.addSong(data, "media/" + songaudio_file.name)
        delete_file('media/' + songaudio_file.name)

    #     # Save the Song object
        # song = Song.objects.create(
        #     song_artist=artist,
        #     song_name=song_name,
        #     popularity=0,
        #     songaudio_file_urn=url  # You can change this field to store the duration if needed.
        # )

        

    #     return redirect('artist_page')  # Replace 'artist_page' with the URL name of the page you want to redirect to after successful submission

    return render(request, "artist_page.html", context)  # Replace 'artist_form' with the name of your template for the artist form


def play(request):
    context.clear()
    session_status(request)
    if request.method == "POST":
        output = request.POST.get("submit").split(",")
        context["Song"] = output[0]
        context["Artist"] = output[1]
        context["url"] = output[2]
        print(context)
    
    return render(request, "play.html", context)

    
def albums(request):
    return render(request, "albums.html")

def playlist(request):
    return HttpResponse("hello this is playlist")

def liked_songs(request):
    return render(request, "liked_songs.html")

def my_account(request):
    return render(request, "my_account.html")

def my_uploads(request):
    return render(request, "my_uploads.html")

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
    # context = {}
    context.clear()
    session_status(request)

    if request.method == 'POST':
        val = request.POST.get('val')
        context['data'] = firebase_functions.searchSong(val)
        # count = 1
        if len(context['data'])!=0:
            return render(request, "search.html", context)
    

    return render(request, "search.html")
# Create your views here.
