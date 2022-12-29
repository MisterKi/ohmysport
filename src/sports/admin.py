from django.contrib import admin
from .models import Sport, Team, Post

# Register your models here.
admin.site.register([Sport, Team, Post])
