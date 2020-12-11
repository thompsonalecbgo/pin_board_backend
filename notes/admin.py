from django.contrib import admin

from .models import Note, Link

admin.site.register(Note)
admin.site.register(Link)