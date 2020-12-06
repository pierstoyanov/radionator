from django.contrib import admin

# Register your models here.

from radio.models import RadioStation, FavouritesList, BackgroundChoice

admin.site.register(RadioStation)
admin.site.register([FavouritesList, BackgroundChoice])
