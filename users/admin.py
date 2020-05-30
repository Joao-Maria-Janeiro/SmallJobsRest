from django.contrib import admin
from .models import UserProfile, Skill

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Skill)