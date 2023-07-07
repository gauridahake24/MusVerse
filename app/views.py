from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def artist(request):
    return render(request, "artist_page.html")

def playlist(request):
    return HttpResponse("hello this is playlist")

def liked_songs(request):
    return HttpResponse("hello this is liked songs")


