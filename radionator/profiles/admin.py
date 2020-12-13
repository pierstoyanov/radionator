from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from radionator.profiles.models import Profile

RadioUser = get_user_model()


class ProfileInlineAdmin(admin.StackedInline):
    """This class includes the Profile model as part of the user admin"""
    model = Profile
    verbose_name_plural = 'Profile (Extended user info)'


class Moderator(UserAdmin):
    """"Moderator is the UserAdmin model that manages the users."""
    inlines = (
        ProfileInlineAdmin,
    )


admin.site.unregister(RadioUser)
admin.site.register(RadioUser, Moderator)

