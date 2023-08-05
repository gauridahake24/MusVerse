from django.contrib import admin
from django.urls import path 
from new_app import views


urlpatterns = [
    path("admin/",admin.site.urls),
    path("",views.home, name ="home"),
    path("playlist/",views.playlist, name ="playlist"),
    path("liked_songs",views.liked_songs, name = "liked_songs"),
    path("artist",views.artist, name = "artist_page"),
    path("login",views.login, name = "login"),
    path("logout", views.logout, name = "logout"),
    path("search", views.search, name = "search"),
    path("play", views.play, name = "play"),
    path('liked-songs', views.liked_songs, name='liked-songs'),
    path('my_account', views.my_account, name='my_account'),
    path('my_uploads', views.my_uploads, name='my_uploads'),
    
]
