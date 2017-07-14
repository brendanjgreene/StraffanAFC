from django.contrib import admin
from models import Player, Team, StaffTitle, Profile

# Register your models here.
admin.site.register(Player, Profile)
admin.site.register(Team)
admin.site.register(StaffTitle)
