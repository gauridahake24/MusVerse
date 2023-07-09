from django.contrib import admin
from django.urls import path 
from new_app import views

urlpatterns = [
    path("admin/",admin.site.urls),
    path("",views.home, name ="home"),
    path("playlist/",views.playlist, name ="playlist"),
    path("liked_songs",views.liked_songs, name = "liked_songs"),
    path("artist",views.artist, name = "artist"),
    path("log_in",views.log_in, name = "log_in"),
    path("albums",views.albums, name = "albums")
    
]
