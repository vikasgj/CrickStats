from django.contrib import admin
from .models import Team, Player,Record

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'country']

# @admin.register(Match)
# class MatchAdmin(admin.ModelAdmin):
#     list_display = ['id', 'date', 'format', 'team1', 'team2']

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'player','runs', 'wickets']
