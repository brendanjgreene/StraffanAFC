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
            'name': forms.TextInput(attrs={'placeholder': 'enter First Name'}),
            'date_of_birth': forms.DateInput(attrs={
                'placeholder': 'MM/DD/YYY',
                'id': 'date',
            }),
            'last_name': forms.TextInput(attrs={'placeholder': 'enter Last Name'}),
            'parent_name': forms.TextInput(attrs={'placeholder': 'enter Parents Full Name'}),
            'mobile': forms.TextInput(attrs={'placeholder': 'enter Parents Full Name'}),
            'parent_name': forms.TextInput(attrs={'placeholder': 'enter Parents Full Name'})
        }


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


