from django.shortcuts import render, get_object_or_404
from models import Player, Team
from forms import TeamForm, PlayerForm, UserLoginForm, TeamDeleteForm
from django.shortcuts import redirect
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from news.forms import SubjectFormDesc
from django.contrib.auth.models import User


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
        team_form = TeamForm(request.POST)
        subject_form_desc = SubjectFormDesc(request.POST)
        if team_form.is_valid() and subject_form_desc.is_valid():
            team = team_form.save(commit=False)
            team.save()
            subject = subject_form_desc.save(commit=False)
            subject.name = team.name
            subject.team_id = team.id
            subject.save()

            messages.success(request, "You have added the " + team.name + " Team!")

            return redirect("get_team", team.id)
    else:
        team_form = TeamForm()
        subject_form_desc = SubjectFormDesc()
    return render(request, 'team_subject_form.html', {'team_form': team_form,
                                                      'subject_form_desc': subject_form_desc,
                                                      'heading_text': 'You are creating a new Team!',
                                                      'button_text': 'Save Team',
                                                      'teams': Team.objects.all().order_by("-name")})


def edit_team(request, id):
    team = get_object_or_404(Team, pk=id)
    if request.method == "POST":
        form = TeamForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            team = form.save(commit=False)
            team.save()
            messages.success(request, "the " + team.name + " was edited!")

            return redirect(reverse('get_team', args={team.pk}))
    else:
        form = TeamForm(instance=team)

    return render(request, 'form.html', {'form': form,
                                         'heading_text': 'You are editing ' + team.name + 'Team?',
                                         'button_text': 'Save Changes',
                                         'teams': Team.objects.all().order_by("-name")})


def delete_team(request, id):
    team = get_object_or_404(Team, pk=id)
    if request.method == "POST":
        form = TeamDeleteForm(request.POST, instance=team)
        team.delete()

        messages.success(request, "The " + team.name + " team was deleted!")

        return redirect("get_teams")
    else:
        form = TeamDeleteForm(instance=team)

    return render(request, 'form.html', {'form': form,
                                         'heading_text': 'Are you sure you want to delete the '
                                                         + team.name +
                                                         ' Team?  All of the Players and News Associated with this '
                                                         'team will also be deleted.  '
                                                         'We suggest you reassign these players and other items first!',
                                         'button_text': 'Click to confirm deletion of ' + team.name + ' Team',
                                         'teams': Team.objects.all().order_by("-name")})


def new_player(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.save()

            messages.success(request, "You have added " + player.name + " " + player.last_name + " to " + player.team.name + " Team!")

            return redirect('get_team', player.team_id)
    else:
        form = PlayerForm()

    return render(request, 'form.html', {'form': form,
                                         'heading_text': 'You are creating a new player!',
                                         'button_text': 'Save Player',
                                         'teams': Team.objects.all().order_by("-name")})


def edit_player(request, id):
    player = get_object_or_404(Player, pk=id)
    if request.method == "POST":
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            player = form.save(False)
            player.save()
            messages.success(request, "You have edited " + player.name + ' ' + player.last_name + "!")

            return redirect('get_team', player.team_id)
    else:
        form = PlayerForm(instance=player)

    return render(request, 'form.html', {'form': form,
                                         'heading_text': 'You are editing ' + player.name + ' ' + player.last_name,
                                         'button_text': 'Save Player',
                                         'teams': Team.objects.all().order_by("-name")})


def delete_player(request, id):
    player = get_object_or_404(Player, pk=id)
    if request.method == "POST":
        form = TeamForm(request.POST, instance=player)
        player.delete()

        messages.success(request, player.name + ' ' + player.last_name + " was deleted!")

        return redirect('get_team', player.team_id)

    else:
        form = PlayerForm(instance=player)

    return render(request, 'form.html', {'form': form,
                                         'heading_text': 'Are you sure you want to delete ' + player.name + ' ' + player.last_name + "!",
                                         'button_text': 'confirm delete ' + player.name + ' ' + player.last_name + "!",
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
    return render(request, "team.html",
                  {'team_name': team_name,
                   'managers_list': User.objects.all(),
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


