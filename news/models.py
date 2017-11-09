from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.conf import settings
from home.models import Team
from PIL import Image, ExifTags
from PIL.ImageOps import fit
from django.core.files.storage import default_storage as storage


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

    class Meta:
        ordering = ['-created_at']

    def __unicode__(self):
        return self.name


class Post(models.Model):

    thread = models.ForeignKey(Thread, related_name='posts')
    comment = HTMLField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    created_at = models.DateTimeField(default=timezone.now)

    image = models.ImageField(upload_to="images", blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        ordering = ['-created_at']

    def __unicode__(self):
        return self.comment

    def save(self, **kwargs):
        super(Post, self).save()
        if self.image:
            image = Image.open(storage.open(self.image.name))
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

            basewidth = 500
            wpercent = (basewidth / float(image.size[0]))
            hsize = int((float(image.size[1]) * float(wpercent)))
            image = image.resize((basewidth, hsize), Image.ANTIALIAS)

            # image = fit(image, (400, 400), Image.ANTIALIAS)
            fh = storage.open(self.image.name, "wb")
            format = 'png'  # You need to set the correct image format here
            image.save(fh, format)
            fh.close()
