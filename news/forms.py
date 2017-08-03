from django import forms
from .models import Thread, Post, Subject
from tinymce.models import HTMLField


class StoryForm(forms.ModelForm):
    name = forms.CharField(label="Story Title")
    is_a_poll = forms.BooleanField(label="Include a poll?", required=False)

    class Meta:
        model = Thread
        fields = ['name']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['comment', 'image']


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'description', 'team']


class SubjectFormDesc(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['description']


