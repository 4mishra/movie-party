from django.contrib import admin
from .models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):
    pass


class MovieAdmin(admin.ModelAdmin):
    pass


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
