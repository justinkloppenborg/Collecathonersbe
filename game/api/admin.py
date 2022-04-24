from django.contrib import admin
from .models import Game


class GameList(admin.ModelAdmin):
    list_display = ('name', 'console', 'description', 'paid')
    list_filter = ('name', 'console', 'paid')
    search_fields = ('name', 'console')
    ordering = ['name']


admin.site.register(Game, GameList)