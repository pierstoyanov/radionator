from django.contrib import admin

# Register your models here.

from radionator.radio.models import RadioStation, FavouritesList

admin.site.register(RadioStation)
admin.site.register([FavouritesList])
