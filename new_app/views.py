from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from .models import User

# Create your views here.
def home(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        arr = User.objects.filter(email = email)[0]
        name = arr.username
        id = arr.userid
        print(name)
        print(id)
        context = {
            "name": name,
            "id": id
        }
        
    return render(request, "home.html", context)

def artist(request):
    return render(request, "artist_page.html")

def login(request):
    return render(request, "log_in.html")
    
def albums(request):
    return render(request, "albums.html")

def playlist(request):
    return HttpResponse("hello this is playlist")

def liked_songs(request):
    return HttpResponse("hello this is liked songs")

def login(request):
    return render(request, "log_in.html")

# Create your views here.
