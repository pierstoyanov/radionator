from django.contrib import admin

# Register your models here.
from profiles.models import UserProfile

admin.site.register(UserProfile)
