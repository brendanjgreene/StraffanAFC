from django import forms
from models import Team, Player
from news.models import Subject
from django.contrib.auth.forms import UserCreationForm


class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ['name']


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
                'placeholder': 'MM/DD/YYYY',
                'id': 'date',
            }),
        }


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


