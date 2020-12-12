from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from radionator.radio.models import PlayList


class CreatePlayList(CreateView):
    """View to create an new PlayList object"""
    model = PlayList
    template_name = 'radio/playlist_create.html'
    fields = '__all__'

    success_url = reverse_lazy('radio index')


#TODO edit pemissions
class PlayListDetails(DetailView):
    """View to display a PlayList object.
    User can edit self.playlists.
    Elevated can edit any playlist."""
    model = PlayList
    template_name = 'radio/playlist_details.html/'


#TODO Edit Delete foor elevated users only


class EditPlayList(UpdateView):
    """Change the RadioStations in the Playlist. Returns MSG if successful"""
    model = PlayList
    fields = '__all__'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO,
                             f'PlayList {self.object.name} edited successfully.')
        return reverse_lazy('radio index')


class DeletePlayList(DeleteView):
    """Delete the PlayList object. Returns MSG if successful"""
    model = PlayList

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO,
                             f'PlayList {self.object.name} DELETED successfully. :(')
        return reverse_lazy('radio index')
