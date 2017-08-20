from __future__ import unicode_literals
from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Club(models.Model):

    class Meta:
        app_label = "club"

    name = models.CharField(max_length=255)
    description = HTMLField()
    mainColor = models.CharField(max_length=255)
    secondColor = models.CharField(max_length=255)
    clubLogo = models.ImageField(upload_to="images", blank=True, null=True)
    backgroundImage = models.ImageField(upload_to="images", blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    homefield = models.CharField(max_length=50, blank=True, null=True)
    long = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    lat = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)

    def __unicode__(self):
        return self.name
