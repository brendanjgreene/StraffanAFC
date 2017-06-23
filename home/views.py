from django.shortcuts import render, get_object_or_404
from models import Player, Team, AccountUserManager
from forms import TeamForm, PlayerForm, UserLoginForm
from django.shortcuts import redirect
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.contrib.auth.models import UserManager


'''def new_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'blogpostform.html', {'form': form})'''


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your username or password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form': form, 'teams': Team.objects.all().order_by("-name")}
    args.update(csrf(request))
    return render(request, 'login.html', args)


def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def new_team(request):
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            Team = form.save(commit=False)
            Team.save()

            messages.success(request, "You have added a new Team!")

            return redirect("/")
    else:
        form = TeamForm()
    return render(request, 'team-form.html', {'form': form})


def edit_team(request, id):
    team = get_object_or_404(Team, pk=id)
    if request.method == "POST":
        form = TeamForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            team = form.save(False)
            team.save()
            messages.success(request, "You have edited the team!")

            return redirect('teams')
    else:
        form = TeamForm(instance=team)

    return render(request, 'team-form.html', {'form': form,
                                              'teams': Team.objects.all().order_by("-name")})


def new_player(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            Player = form.save(commit=False)
            Player.save()

            messages.success(request, "You have added a new player!")

            return redirect(get_players)
    else:
        form = PlayerForm()
    return render(request, 'player-form.html', {'form': form,
                                                'teams': Team.objects.all().order_by("-name")})


def edit_player(request, id):
    player = get_object_or_404(Player, pk=id)
    if request.method == "POST":
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            player = form.save(False)
            player.save()
            messages.success(request, "You have edited a Player!")

            return redirect('players')
    else:
        form = PlayerForm(instance=player)

    return render(request, 'player-form.html', {'form': form,
                                                'teams': Team.objects.all().order_by("-name")})


def get_index(request):
    return render(request, 'index.html',
                  {'teams': Team.objects.all().order_by("-name")})


def get_players(request):
    return render(request, "players.html",
                  {'player_list': Player.objects.all().order_by("-date_of_birth"),
                   'teams': Team.objects.all().order_by("-name")})


def get_team(request, id):
    team_name = get_object_or_404(Team, pk=id)
    return render(request, "teams.html",
                  {'team_name': team_name,
                   'team_list': Player.objects.filter(team__id=id),
                   'teams': Team.objects.all().order_by("-name")})


def get_teams(request):
    return render(request, "teams.html",
                  {'teams': Team.objects.all().order_by("-name"),
                   'team_list': Player.objects.all()})


def get_info(request):
    return render(request, 'about.html',
                  {'teams': Team.objects.all().order_by("-name")})


@login_required(login_url='/login/')
def profile(request):
    return render(request, 'profile.html',
                  {'teams': Team.objects.all().order_by("-name")})


