from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.conf import settings
from home.models import Team


class Subject(models.Model):

    name = models.CharField(max_length=255)
    description = HTMLField()
    team = models.ForeignKey(Team, related_name='subject_team')

    def __unicode__(self):
        return self.name


class Thread(models.Model):

    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='threads')
    subject = models.ForeignKey(Subject, related_name='threads')
    created_at = models.DateTimeField(default=timezone.now)


class Post(models.Model):

    thread = models.ForeignKey(Thread, related_name='posts')
    comment = HTMLField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    created_at = models.DateTimeField(default=timezone.now)