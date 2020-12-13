from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from common.BackgroundMixin import BackgroundMixin
from radionator.radio.models import PlayList

RadioUser = get_user_model()


class CreatePlayList(BackgroundMixin, LoginRequiredMixin, CreateView):
    """View to create an new PlayList object"""
    model = PlayList
    template_name = 'radio/playlist_create.html'
    fields = ('list_name', 'is_user_default', 'radio_stations')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO,
                             f'PlayList {self.object.list_name} created successfully.')
        return reverse('playlists', kwargs={'pk': self.request.user.pk})


class PlayListDetails(BackgroundMixin, LoginRequiredMixin, DetailView):
    """View to display a PlayList object. User can edit self.playlists.
    Elevated can edit any playlist."""
    model = PlayList
    template_name = 'radio/playlist_details.html/'


class EditPlayList(BackgroundMixin, LoginRequiredMixin, UpdateView):
    """Change the RadioStations in the Playlist. Returns MSG if successful"""
    model = PlayList
    fields = '__all__'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO,
                             f'PlayList {self.object.name} edited successfully.')
        return reverse('playlists', kwargs={'pk': self.request.user.pk})


class DeletePlayList(BackgroundMixin, LoginRequiredMixin, DeleteView):
    """Delete the PlayList object. Returns MSG if successful"""
    model = PlayList

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO,
                             f'PlayList {self.object.name} DELETED successfully. :(')
        return reverse_lazy('radio index')
