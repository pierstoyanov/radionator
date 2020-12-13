from django.contrib import admin

# Register your models here.

from radionator.radio.models import RadioStation, PlayList


class RadioStationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class PlayListAdmin(admin.ModelAdmin):
    fields = ['radio_stations',]
    list_display = ('id', 'list_name', 'user', 'get_radio_stations')

    def get_radio_stations(self, obj):
        """This function retrieves all radio stations connected to the playlist."""
        return "\n".join([s.stations for s in obj.radio_stations.all()])


admin.site.register(PlayList, PlayListAdmin)
admin.site.register(RadioStation)

