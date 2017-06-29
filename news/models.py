from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.conf import settings
from home.models import Team


class Subject(models.Model):

    name = models.CharField(max_length=255)
    description = HTMLField()
    team = models.ForeignKey(Team, blank=True, null=True, related_name='subject_team')

    def __unicode__(self):
        return self.name


class Thread(models.Model):

    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='threads')
    subject = models.ForeignKey(Subject, related_name='threads')
    created_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.name


class Post(models.Model):

    thread = models.ForeignKey(Thread, related_name='posts')
    comment = HTMLField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    created_at = models.DateTimeField(default=timezone.now)

    image = models.ImageField(upload_to="images", blank=True, null=True)
    # requires from settings import MEDIA_ROOT in url.py and
    # MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    # MEDIA_URL = '/media/' in settings

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.comment
