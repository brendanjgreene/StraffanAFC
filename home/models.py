from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone


class Team(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class StaffTitle(models.Model):

    class Meta:  # include this to ensure build in IDE
        app_label = "home"

    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=True,
                                   help_text='Designates whether the user can log into this admin site.')
    is_superuser = models.BooleanField(default=False,
                                       help_text='Designates whether the user can log into all admin site.')

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


class AccountUserManager(UserManager):
    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
       Creates and saves a User with the given username, email and password.
       """
        now = timezone.now()
        if not email:
            raise ValueError('The given username must be set')

        email = self.normalize_email(email)
        user = self.model(username=email, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, team=models.ForeignKey(Team, related_name='user_name'), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

