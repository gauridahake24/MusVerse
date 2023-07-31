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
import firebase_admin
from firebase_admin import credentials, firestore, storage
import os
import tempfile

serviceAccountKey = {
  "type": "service_account",
  "project_id": "musverse-784e4",
  "private_key_id": "c4fcd75cc1678595a495dd91fe556b5f11b0e6c9",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCojRY/DSuJ1KtI\n2oSZtZLxEKIWXpDiGjttmDUTjy4ISYWlv8DyIW6cVg9ICRAn2WJcE4PW6lWm8YUp\nlkvbW5XTCAoiofiYWysR/yezdFGgCFa55fd9lgIrg+6PmHItj6lsFXoji5B/aMQa\nha+RP1R7QYZB0Lpqn5kPWzbHJIIdjl5KZIbvButRJQe14vvJx9plqjzAmI5/ia3U\nXQ+oPwloqvEn0RjTxp5699wZGixnb8Q3CGDjiRhKwoaytXERj35APGoIjymuCCkA\nnEdWHx4+vcRX0URYh1N5YFPkz1kS87nh687zeYDGmhG7AHaFeK6u5pAh13rsAGAk\nnppOjKOhAgMBAAECggEAAS8YBtkl0GqaidOzSp/eFHnKygQlKa8YMlBx/3/yCXp9\nkQeY5a6EJWlHQ1OWeKbavYrgzO68QNS5nBbyCUGnqqntMHdMLML3rraTecu1cChc\n1m0/TOiucwMtduEMkhsRgZNgoQfVAT3GzQj56IKYuk1VwcgN64EGXoduz00XfvkE\nYZKXPZPqHv1oVaU57CfGCTmC/wbWr6AA5j+cfdaYvqwIa0wuptF8Oe4DJFHvNH97\nfS8/V27eyDxK0KvkMYx7V7bb48GF1asijltaoOV2Nw1KD/zNJ/1U1uk6+Waq6uXq\nibkmlpEm8OBO+YURK5N3cqNbcuf+0zphvLdspjl9MQKBgQDk3iHQEerXCe4JtNz6\nNhlrFEcnbEZ9qBngktIs0EUV7Oi91o0nVJtysmphoAcvm1aMlflC9Xv8CRqQjcKQ\nN5eVs8fzCQQLP5bTKTY3qTxpdLFpZcJxubGcJU2pX4df1kmSJKeaWRFM2isWzGPY\nSvn/Kivl1nKVy5EFRB67thB6EQKBgQC8iGq3yhrMa+atJ9XJA4tLZJeRu+RlpJOB\ncNnSeoDrd7YlvbeAAcw0cER/ZbInwiKbzpLWsiRM3g/4HGBsOI6xfZhDcwciooAt\nueIOGXtuVN9OVmGN7oOCY0q4uHqNMNjy7+qm4Ao95PMipjQm9aMPza+TecExmrT0\nne7raD+AkQKBgBQXL86tE/lmhL/TYaaRQy/0Kr7aMWHsdMETAmIusjHXhyLLB78R\nHUg3Q0Foo9jZAQL8U1I+bHDWd7+CwjaYurTIgF/kRbebEGle78R5FbWIKd6/sQ78\npwu29pdMrHyMOg8bKp9Q/ETLzgaFUKp3AnUUxZ+6cHqX0RYuQahmthGRAoGATIVy\nCzbUubPx5MYOV5BAsVEa0+PXSAoMdLVBM9TVDr2ACMGAAUy5fW8z3iGAtfJt6Z9m\nqg2T/j8DbEjYOhSalh/L9VRyyPP74pNX1TEykA2StVEKN3lfl0SFx4PY+gWhiLko\nHKNChOywYpfjAw0gKgHqCYmZiHCqkb6ogpPFcoECgYEAtWqX1TAnaIG/+6nG4j5i\nO9CHS3puZ3oMCkMvwAqSJNoJV5GdqP3yumCtn9P7jWGS4h8dfMVsO/u/taikcb5T\n64OEFM6xqPakBGGex2ahh7H7dz/0ad4PgydRf/gKjO70i0AZ16nyZrk0cp4qCcWS\nHlWJFheuolpe3HBFEtLK+CA=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-bvxpp@musverse-784e4.iam.gserviceaccount.com",
  "client_id": "115347137708460813022",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-bvxpp%40musverse-784e4.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

cred = credentials.Certificate(serviceAccountKey)

config = {
    "apiKey": "AIzaSyA0FjpJuSmEuXXKGfcRUQ2YQv_B3ShPsSw",
    "authDomain": "musverse-784e4.firebaseapp.com",
    "projectId": "musverse-784e4",
    "storageBucket": "musverse-784e4.appspot.com",
    "messagingSenderId": "681171328905",
    "appId": "1:681171328905:web:421eed50799c026ec58b58",
    "measurementId": "G-M7LN6BW495",
    "serviceAccount": cred,
}


# Create your views here.
def session_status(request):
    if 'login_status' in request.COOKIES and 'username' in request.COOKIES:
        context['login_status'] = request.COOKIES.get('login_status')
        context['username'] = request.COOKIES['username']

    


def home(request):
    global context
    context = {}
    session_status(request)
    # if 'login_status' in request.COOKIES and 'username' in request.COOKIES:
    #     context['login_status'] = request.COOKIES.get('login_status')
    #     context['username'] = request.COOKIES['username']
    #     return render(request, "home.html", context)

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
            song = Song.objects.get(pk=song_id)
            user = request.user
            liked_song, created = LikedSong.objects.get_or_create(uid=user)
            liked_song.liked_songs.add(song)
            return redirect('liked-songs')  
    return redirect('home') 

def upload_to_firestore(request, fileName):
    Fire_app = firebase_admin.initialize_app(cred,config)

    data = {
        "artist_name": request.POST.get('artist_name'),
        "song_name": request.POST.get('song_name')
    }
    
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    blob.make_public()
    url = blob.public_url

    firebase_admin.delete_app(Fire_app)
    return url


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
        artist_name = request.POST.get('artist_name')
        song_name = request.POST.get('song_name')
        # songaudio_file = request.FILES.get('songaudio_file')
        duration = request.POST.get('duration')
        songaudio_file = request.FILES['songaudio_file']

        # Check if the uploaded file is empty
        if not songaudio_file:
            return render(request, "error.html", {'error_message': 'No audio file selected.'})

        # Save the Artist object
        artist, created = Artist.objects.get_or_create(artist_name=artist_name)
        
        with open('media/' + songaudio_file.name, 'wb+') as destination_file:
            for chunk in songaudio_file.chunks():
                destination_file.write(chunk)
        
        url = upload_to_firestore(request, 'media/' + songaudio_file.name)
        print(url)

    #     # Save the Song object
        song = Song.objects.create(
            song_artist=artist,
            song_name=song_name,
            popularity=0,
            songaudio_file_urn=url  # You can change this field to store the duration if needed.
        )

        delete_file('media/' + songaudio_file.name)

        

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
        # count = 1
        if len(Song.objects.filter(song_name__icontains = val).order_by('-popularity'))!=0:
            context['data'] = []
            arr = Song.objects.filter(song_name__icontains = val).order_by('-popularity')
            for i in arr:
                temp = {"Song": i.song_name, "Artist": i.song_artist, "Popularity": i.popularity, "url":i.songaudio_file_urn}
                context['data'].append(temp)
                print(i.song_artist)
            # print(context)
            return render(request, "search.html", context)
    

    return render(request, "search.html")
# Create your views here.
