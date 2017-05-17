from django.shortcuts import render
from models import Player


def get_index(request):
    return render(request, 'index.html')


def get_players(request):
    return render(request, "players.html",
                  {'player_list': Player.objects.all()})


def get_team(request):
    return render(request, "team.html",
                  {'team_list': Player.objects.get(team="U11 White")})

