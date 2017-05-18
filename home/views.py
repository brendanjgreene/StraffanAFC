from django.shortcuts import render
from models import Player, Team


def get_index(request):
    return render(request, 'index.html',
                  {'teams': Team.objects.all().order_by("-name")})


def get_players(request):
    return render(request, "players.html",
                  {'player_list': Player.objects.all()})


def get_team(request):
    return render(request, "team.html",
                  {'team_list': Player.objects.filter(team__exact="name")})


def get_team_test(request):
    return render(request, "team.html",
                  {'team_list': Player.objects.filter(team__id=1),
                   'teams': Team.objects.all().order_by("-name")})


def get_info(request):
    return render(request, 'about.html')


def profile(request):
    return render(request, 'profile.html')
