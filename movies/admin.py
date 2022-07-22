from django.contrib import admin
from .models import Genre, Movie

class GenreAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')

class MovieAdmin(admin.ModelAdmin):
  exclude = ('date_created',)
  list_display = ('title', 'overview','genre','url', 'release_date', 'vote_average','vote_count')

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)