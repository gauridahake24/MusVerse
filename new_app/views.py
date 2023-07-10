from django.shortcuts import render, reverse
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from .models import User
from .models import Artist
from datetime import timedelta




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
        extension = str(songaudio_file).split(".")  
        if extension[1] != "mp3":
            return render(request, "home.html")
        # duration = request.POST.get('duration')
    
        
        new_artist = Artist(artist_name=artist_name, song_name=song_name, songaudio_file=songaudio_file)
        new_artist.save()
        
        return render(request, "home.html")
    
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
# Create your views here.
