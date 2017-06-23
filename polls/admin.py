from django.contrib import admin
from .models import Poll
from .models import PollSubject

admin.site.register(Poll)
admin.site.register(PollSubject)
