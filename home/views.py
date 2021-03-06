from django.shortcuts import render, get_object_or_404
from models import Player, Team, Profile
from forms import TeamForm, PlayerForm, UserLoginForm, TeamDeleteForm, NewUserForm, \
    MyUserChangeForm, MyPasswordChangeForm, ProfileForm, PlayerDeleteForm
from django.shortcuts import redirect
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from news.forms import SubjectFormDesc
from news.models import Subject, Post
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.conf.urls import url
from PIL import Image, ExifTags


def change_your_password(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST, )
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, request.user.username + '. Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(request.user)

    args = {'form': form,
            'cancelview': 'profile',
            'heading_text': request.user.username + ": " + request.user.first_name + " Are you sure you want to change your password",
            'button_text': 'Confirm Password Change',
            }

    return render(request, 'form.html', args)


def edit_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        form = MyUserChangeForm(request.POST, instance=request.user)
        second_form = ProfileForm(request.POST or None, request.FILES, instance=profile)
        if form.is_valid() and second_form.is_valid():
            form.save()
            second_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect(reverse('profile'))
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = MyUserChangeForm(instance=request.user)
        second_form = ProfileForm(instance=profile)

    args = {'form': form,
            'cancelview': 'profile',
            'second_form': second_form,
            'heading_text': 'You are editing user ' + request.user.first_name + " " + request.user.last_name,
            'button_text': 'Save Changes',
            }

    return render(request, 'form.html', args)


@csrf_protect
def new_user(request):
    if not request.user.is_superuser:
        messages.error(request, "you are not authorized to create users")
        return redirect('profile')

    else:
        if request.method == 'POST':
            form = NewUserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.email
                user.is_staff = True
                user.save()
                messages.success(request, "You have created a new user: " + user.username)

                return redirect(reverse('profile'))

            else:
                messages.error(request, 'Please correct the errors below.')

        else:
            form = NewUserForm()

        args = {'form': form,
                'cancelview': 'profile',
                'heading_text': 'You are creating a new User!',
                'button_text': 'Save User',
                }

        return render(request, 'form.html', args)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=request.POST.get('username'))
            if user is not None:
                try:
                    Profile.objects.get(user=user)
                except Profile.DoesNotExist:
                    Profile.objects.create(user=user)
                Profile.objects.create(user=user)
            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password'))

            if user is not None:
                try:
                    Profile.objects.get(user=user)
                except Profile.DoesNotExist:
                    Profile.objects.create(user=user)
                auth.login(request, user)
                messages.success(request, "You have successfully logged in")
                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your username or password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form': form}
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
            subject = subject_form_desc.save(commit=False)
            subject.name = team.name
            team.save()  # needs to be here so team.id is created before subject.team_id
            subject.team_id = team.id
            subject.save()

            messages.success(request, "You have added the " + team.name + " Team!")

            return redirect("get_team", team.id)

        else:
            messages.error(request, 'Please correct the errors below.')

    else:
        team_form = TeamForm()
        subject_form_desc = SubjectFormDesc()

    '''delete this when im sure form.html working
    return render(request, 'team_subject_form.html', {'team_form': team_form,
                                                      'cancelview': 'profile',
                                                      'subject_form_desc': subject_form_desc,
                                                      'heading_text': 'You are creating a new Team!',
                                                      'button_text': 'Save Team',
                                                      })'''

    return render(request, 'form.html', {'form': team_form,
                                         'second_form': subject_form_desc,
                                         'cancelview': 'profile',
                                         'heading_text': 'You are creating a new Team!',
                                         'button_text': 'Save Team',
                                         })


def edit_team(request, id):
    team = get_object_or_404(Team, pk=id)
    subject = get_object_or_404(Subject, team_id=id)
    if request.method == "POST":
        form = TeamForm(request.POST, request.FILES, instance=team)
        second_form = SubjectFormDesc(request.POST, request.FILES, instance=subject)
        if form.is_valid() and second_form.is_valid():
            team = form.save(commit=False)
            subject = second_form.save(commit=False)
            subject.name = team.name
            subject.team_id = team.id
            subject.save()
            team.save()
            messages.success(request, "the " + team.name + " was edited!")

            return redirect(reverse('get_team', args={team.pk}))
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = TeamForm(instance=team)
        second_form = SubjectFormDesc(instance=subject)

    return render(request, 'form.html', {'form': form,
                                         'cancelview': 'get_team',
                                         'cancelid': team.id,
                                         'second_form': second_form,
                                         'heading_text': 'You are editing the ' + team.name + ' Team?',
                                         'button_text': 'Save Changes',
                                         })


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
                                         'cancelview': 'get_team',
                                         'cancelid': team.id,
                                         'heading_text': 'Are you sure you want to delete the '
                                                         + team.name +
                                                         ' Team?  All of the Players and News Associated with this '
                                                         'team will also be deleted.  '
                                                         'We suggest you reassign these players and other items first!',
                                         'button_text': 'Click to confirm deletion of the ' + team.name + ' Team',
                                         })


def new_player(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)

        if form.is_valid():
            player = form.save(commit=False)
            player.save()

            messages.success(request, "You have added " + player.name + " " + player.last_name + " to " + player.team.name + " Team!")

            return redirect('get_team', player.team_id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PlayerForm()
        if request.user.is_superuser:
            form.fields['team'].queryset = Team.objects.all()
        else:
            form.fields["team"].queryset = Team.objects.filter(id=request.user.profile.team_id)

    return render(request, 'form.html', {'form': form,
                                         'heading_text': 'You are creating a new player!',
                                         'button_text': 'Save Player',
                                         })


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
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PlayerForm(instance=player)
        if request.user.is_superuser:
            form.fields['team'].queryset = Team.objects.all()
        else:
            form.fields['team'].queryset = Team.objects.filter(id=request.user.profile.team_id) | Team.objects.filter(name="Unassigned")

    return render(request, 'form.html', {'form': form,
                                         'cancelview': "get_team",
                                         'cancelid': player.team.id,
                                         'heading_text': 'You are editing ' + player.name + ' ' + player.last_name,
                                         'button_text': 'Save Player',
                                         })


def delete_player(request, id):
    player = get_object_or_404(Player, pk=id)
    if request.method == "POST":
        form = PlayerDeleteForm(request.POST, instance=player)
        player.delete()

        messages.success(request, player.name + ' ' + player.last_name + " was deleted!")

        return redirect('get_team', player.team_id)

    else:
        form = PlayerDeleteForm(instance=player)

    return render(request, 'form.html', {'form': form,
                                         'cancelview': "get_team",
                                         'cancelid': player.team.id,
                                         'heading_text': 'Are you sure you want to delete ' + player.name + ' ' + player.last_name + "!",
                                         'button_text': 'confirm delete ' + player.name + ' ' + player.last_name + "!",
                                         })


def get_index(request):
    images = Post.objects.exclude(image='')
    posts = Post.objects.all().order_by("-created_at")[:10]
    return render(request, 'index.html',
                  {"images": images,
                   "posts": posts})


def get_players(request):
    return render(request, "players.html",
                  {'player_list': Player.objects.all().order_by("-date_of_birth")})


def get_team(request, id):
    team_name = get_object_or_404(Team, pk=id)
    return render(request, "team.html",
                  {'team_name': team_name,
                   'team': Team.objects.filter(id=id),
                   'subjects': Subject.objects.all(),
                   'managers_list': User.objects.filter(profile__team=id),
                   'team_list': Player.objects.filter(team__id=id),
                   })


def get_teams(request):
    return render(request, "teams.html",
                  {'teams': Team.objects.all(),
                   'managers_list': User.objects.all(),
                   'team_list': Player.objects.all()})


def get_info(request):
    return render(request, 'about.html',
                  {'staff': User.objects.filter(is_staff=True).order_by('profile__team__age')})


@login_required(login_url='/login/')
def profile(request):
    return render(request, 'profile.html',
                  {'staff': User.objects.all(),
                   'parents': Player.objects.all()})









