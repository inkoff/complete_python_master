from .models import Genre, Movie
from dataclasses import fields
from django.contrib import admin

# Register your models here.


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created',)
    list_display = ("id", "title", "release_year",
                    "genre", "numbers_in_stock")


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
