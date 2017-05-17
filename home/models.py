from django.db import models


class Player(models.Model):

    class Meta:  # include this to ensure build in IDE
        app_label = "home"

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    parent_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    team = models.CharField(max_length=255)

    def __str__(self):
        return ' '.join([
            self.first_name,
            self.last_name,
        ])