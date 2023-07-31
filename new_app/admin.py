from django.contrib import admin
from new_app.models import Song, Artist, User,liked_songs

# Register your models here.
admin.site.register(Song)
admin.site.register(User)
admin.site.register(Artist)
admin.site.register(liked_songs)


# Register your models here.
