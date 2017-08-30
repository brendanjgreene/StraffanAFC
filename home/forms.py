from django import forms
from models import Team, Player, Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ['name', 'age']


class TeamDeleteForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = []


class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ['name', 'last_name', 'parent_name', 'mobile', 'email', 'date_of_birth', 'team']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "enter Player's First Name"}),
            'last_name': forms.TextInput(attrs={'placeholder': "enter Player's Last Name"}),
            'parent_name': forms.TextInput(attrs={'placeholder': "enter Parent's Full Name if a minor"}),
            'mobile': forms.TextInput(attrs={'placeholder': "enter Mobile or Parent's Mobile if a minor"}),
            'email': forms.TextInput(attrs={'placeholder': "enter Email or Parent's Email if a minor"}),
            'date_of_birth': forms.DateInput(attrs={
                'placeholder': 'mm/dd/yyyy',
                'id': 'date',
            }),
        }


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'unless you changed it your username is your email address'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'unless you changed it your password is your email address'}))


class NewUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email']
        widgets = {'email': forms.TextInput(attrs={'placeholder': "This will also be the username."})}


class MyUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(MyUserChangeForm, self).__init__(*args, **kwargs)
        del self.fields['password']

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(MyPasswordChangeForm, self).__init__(*args, **kwargs)
        del self.fields['old_password']

    class Meta:
        model = User
        exclude = ()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('team', 'mobile', 'title', 'image')
