from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image, ExifTags


class Team(models.Model):

    name = models.CharField(max_length=255)
    age = models.IntegerField()

    class Meta:
        ordering = ['age']

    def __unicode__(self):
        return self.name


class StaffTitle(models.Model):

    class Meta:  # include this to ensure build in IDE
        app_label = "home"

    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Player(models.Model):

    class Meta:  # include this to ensure build in IDE
        app_label = "home"

    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    parent_name = models.CharField(max_length=255,  blank=True, null=True)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=255)
    team = models.ForeignKey(Team, related_name='player_name')

    def __unicode__(self):
        return self.name + " " + self.last_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, related_name='staff_name', blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    title = models.ForeignKey(StaffTitle, related_name='staff_name', blank=True, null=True)

    image = models.ImageField(upload_to="images", blank=True, null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
