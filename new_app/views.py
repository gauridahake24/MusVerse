from django.shortcuts import render, reverse
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from .models import User
from .models import Artist
from datetime import timedelta
import magic
from .models import Song



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

def artist(request):
    if request.method == 'POST':
        artist_name = request.POST.get('artist_name')
        song_name = request.POST.get('song_name')
        songaudio_file = request.FILES.get('songaudio_file')

        extension = magic.from_buffer(songaudio_file.read(), mime=True).split("/")[1]
        print(extension)

        if extension not in ["mpeg", "mp3", "wav", "midi"]:
            return render(request, "home.html")

        artist, created = Artist.objects.get_or_create(artist_name=artist_name)
        song = Song.objects.create(song_artist=artist, song_name=song_name, popularity=0, songaudio_file=songaudio_file)

    return render(request, "artist_page.html")

    
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
