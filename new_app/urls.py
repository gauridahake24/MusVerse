from django.contrib import admin
from django.urls import path 
from new_app import views

urlpatterns = [
    path("admin/",admin.site.urls),
    path("",views.home, name ="home"),
    path("playlist/",views.playlist, name ="playlist"),
    path("liked_songs",views.liked_songs, name = "liked_songs"),
    path("artist",views.artist, name = "liked_songs"),
    path("login",views.login, name = "login")
    
]
