from __future__ import unicode_literals
from django.db import models
from tinymce.models import HTMLField
from PIL import Image, ExifTags
from PIL.ImageOps import fit
from django.core.files.storage import default_storage as storage

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

    def save(self, **kwargs):
        super(Club, self).save()
        if self.backgroundImage:
            image = Image.open(storage.open(self.backgroundImage.name))
            try:
                for orientation in ExifTags.TAGS.keys():
                    if ExifTags.TAGS[orientation]=='Orientation':
                        break
                exif=dict(image._getexif().items())
                if exif[orientation] == 3:
                    image=image.rotate(180, expand=True)
                elif exif[orientation] == 6:
                    image=image.rotate(270, expand=True)
                elif exif[orientation] == 8:
                    image=image.rotate(90, expand=True)
            except (AttributeError, KeyError, IndexError):
                # cases: image don't have getexif
                pass

            image = fit(image, (200, 200), Image.ANTIALIAS)
            fh = storage.open(self.backgroundImage.name, "wb")
            format = 'png'  # You need to set the correct image format here
            image.save(fh, format)
            fh.close()

    def __unicode__(self):
        return self.name
