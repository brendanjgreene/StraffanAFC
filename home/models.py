from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Player(models.Model):

    class Meta:  # include this to ensure build in IDE
        app_label = "home"

    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    parent_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=255)
    team = models.ForeignKey(Team, related_name='player_name')

    def __unicode__(self):
        return self.name + " " + self.last_name
